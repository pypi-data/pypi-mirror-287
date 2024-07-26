import copy
import json
from typing import List

from ultipa.proto.ultipa_pb2 import AttrListData
from ultipa.structs import Property
from ultipa.types.types import ResultType
from ultipa.utils import errors
from ultipa.types import ULTIPA, ULTIPA_RESPONSE, ULTIPA_REQUEST
from ultipa.utils.errors import ParameterException
from ultipa.utils.serialize import _Serialize
from ultipa.utils.typeCheck import TypeCheck


class HasDataMap:
	has_ultipa_data: bool
	has_attr_data: bool
	only_attr_list: bool

	def __init__(self, has_ultipa_data, has_attr_data, only_attr_list):
		self.has_ultipa_data = has_ultipa_data
		self.has_attr_data = has_attr_data
		self.only_attr_list = only_attr_list


class FormatResponse:

	@staticmethod
	def resTableToArray(table: ULTIPA.Table):
		tres = []
		headers = []
		if table:
			try:
				for index, header in enumerate(table.headers):
					if not header.property_name:
						if header.property_type == ULTIPA.PropertyType.PROPERTY_NULL:
							header.property_name = f"null({index})"
					headers.append({"property_name": header.property_name,
									"property_type": Property._getStringByPropertyType(
										header.property_type)})
				tret = ULTIPA.Table(table_name=table.name, headers=headers, table_rows=table.rows)
				tres.append(tret)
			except Exception as e:
				raise errors.ParameterException(e)
		return tret

	@staticmethod
	def formatStatisticsTable(table: ULTIPA.Table):
		headers = []
		if table:
			try:
				for header in table.headers:
					headers.append({"property_name": header.property_name,
									"property_type": Property._getStringByPropertyType(
										header.property_type)})
				item = {}
				for row in table.rows:
					for index in range(len(row)):
						v = row[index]
						item[table.headers[index].property_name] = int(v)
				tret = ULTIPA.UltipaStatistics(edge_affected=item.get("edge_affected"),
											   node_affected=item.get("node_affected"),
											   total_time_cost=item.get("total_time_cost"),
											   engine_time_cost=item.get("engine_time_cost"))
				return tret
			except Exception as e:
				raise errors.ParameterException(e)


class DataMerge:
	@staticmethod
	def arrayDiff(arr1: "[str]", arr2: "[str]"):
		diff = []
		for i in arr2:
			if i not in arr1:
				diff.append(i)
		return diff

	@staticmethod
	def customizer(objValue, srcValue, key, ignoreKeys):
		if ignoreKeys and key in ignoreKeys:
			return objValue

		if isinstance(objValue, list):
			return objValue + srcValue

	@staticmethod
	def merge(o1: object, o2: object, ignoreKeys: [str] = None):
		if ignoreKeys is None:
			ignoreKeys = []
		retDict = {}
		for key in o1:
			if o1.get(key) and o2.get(key):
				mergeRet = DataMerge.customizer(o1[key], o2[key], key, ignoreKeys)
				retDict.update({key: mergeRet})
			else:
				if isinstance(o1, dict) and isinstance(o1, dict):
					if o1.get(key):
						retDict.update({key: o1.get(key)})
						retDict.update(o2)
		return retDict

	@staticmethod
	def concat(arr1: list, arr2: list, bykey: str = None, ignoreKeys: "[str]" = None):

		if bykey:
			if bykey == 'table_name':
				if isinstance(arr1, list) and isinstance(arr2, list):
					newData = arr1
					newArry = arr2

					# Find the different table_name of arr1 and arr2
					if isinstance(newData, dict):
						diff = DataMerge.arrayDiff([i[bykey] for i in arr1], [i[bykey] for i in arr2])
					else:
						diff = DataMerge.arrayDiff([y.name for y in newData], [y.name for y in arr2])

					# If existing, add the table_name to newData
					if diff:
						for di in diff:
							for a2 in arr2:
								if a2.name == di:
									newData.append(ULTIPA.Table(table_name=di, table_rows=a2.rows, headers=a2.headers))

					# Traverse newArry, add table to table_rows in accordance with table_name  
					for a2 in newArry:
						for data in newData:
							if a2.name == data.name:
								data.rows += a2.rows
					return newData

			if bykey == 'nodes':
				if isinstance(arr1, list) and isinstance(arr2, list):
					newArry = arr2
					newData = arr1

					arrtList = []
					for new in newData:
						arrtList.append(new.alias)
					for arr in newArry:
						if arr.alias not in arrtList:
							newData.append(arr)
					for arr in newArry:
						if not newData:
							newData.append(arr)
						for new in newData:
							if arr.alias == new.alias:
								new.nodes += arr.nodes
					return newData

			if bykey == 'edges':
				if isinstance(arr1, list) and isinstance(arr2, list):
					newArry = arr2
					newData = arr1

					arrtlist = []
					for new in newData:
						arrtlist.append(new.alias)

					for arr in newArry:
						if arr.alias not in arrtlist:
							newData.append(arr)
							return newData

					for arr in newArry:
						if not newData:
							newData.append(arr)
						for new in newData:
							if arr.alias == new.alias:
								new.edges += arr.edges

					return newData

			if bykey == 'values':
				if isinstance(arr1, list) and isinstance(arr2, list):
					newArry = arr2
					newData = arr1
					arrtlist = []
					for new in newData:
						arrtlist.append(new.alias)

					for arr in newArry:
						if arr.alias not in arrtlist:
							newData.append(arr)
					for arr in newArry:
						if not newData:
							newData.append(arr)
						for new in newData:
							if arr.alias in arrtlist and arr.alias == new.alias:
								new.values += arr.values
					return newData

			if bykey == 'arrays':
				if isinstance(arr1, list) and isinstance(arr2, list):
					newArry = arr2
					newData = arr1
					arrtlist = []
					for new in newData:
						arrtlist.append(new.alias)

					for arr in newArry:
						if arr.alias not in arrtlist:
							newData.append(arr)

					for arr in newArry:
						if not newData:
							newData.append(arr)
						for new in newData:
							if arr.alias in arrtlist and arr.alias == new.alias:
								new.elements += arr.elements
					return newData

		if isinstance(arr1, list) and isinstance(arr2, list):
			arr1.extend(arr2)
			return arr1
		elif isinstance(arr1, dict) and isinstance(arr2, dict):
			return arr1.update(arr2)


class FormatType:

	@staticmethod
	def checkProperty(row, schemaProperties):
		propertyList = []
		rowPropertyList = row.values.keys()
		for property in rowPropertyList:
			findSchema = list(filter(lambda x: x.get('name') == property, schemaProperties))
			if findSchema:
				schemaProperty = findSchema[0]
				reqProperty = Property(schemaProperty.get("name"))
				reqProperty.setTypeInt(schemaProperty.get("type"))
				propertyList.append(reqProperty)
			else:
				raise ParameterException(
					err=f"row [{row._getIndex()}] error: schema[{row.schema}] doesn't contain property [{property}].")
		return propertyList

	@staticmethod
	def checkNodeRow(i: int, schema: ULTIPA_REQUEST.Schema, row: ULTIPA.EntityRow):
		if row._index != None:
			i = row._index

		if row is None:
			raise ParameterException(err=f"The row [{i}] data is null")

		if row.values is None:
			raise ParameterException(err=f"node row [{i}] error: values are empty but  properties size > 0.")

		if not schema.properties and row.values:
			raise ParameterException(err=f"node row [{i}] error: properties are empty but values size > 0.")

		if len(row.values.keys()) > len(schema.properties):
			raise ParameterException(err=f"node row [{i}] error: values size larger than properties size.")

		if len(row.values.keys()) < len(schema.properties):
			raise ParameterException(err=f"node row [{i}] error: values size smaller than properties size.")

		for proper in schema.properties:
			if proper.isIdType() or proper.isIgnore():
				continue
			if proper.name not in row.values:
				raise ParameterException(
					err=f"node row [{i}] error: values doesn't contain property [{proper.name}].")

	@staticmethod
	def checkEdgeRow(i: int, schema: ULTIPA_REQUEST.Schema, row: ULTIPA.EntityRow):
		if row._index != None:
			i = row._index

		if row is None:
			raise ParameterException(err=f"The row [{i}] data is null")
		if row.values is None:
			raise ParameterException(err=f"edge row [{i}] error: values are empty but properties size > 0.")
		if not schema.properties and row.values:
			raise ParameterException(err=f"edge row [{i}] error: properties are empty but values size > 0.")

		if len(row.values.keys()) > len(schema.properties):
			raise ParameterException(err=f"edge row [{i}] error: values size larger than properties size.")

		if len(row.values.keys()) < len(schema.properties):
			raise ParameterException(err=f"edge row [{i}] error: values size smaller than properties size.")

		if ((row.from_id is None or row.from_id == "") and (row.to_id is None or row.to_id == "")) \
				and (row.from_uuid is None and row.to_uuid is None):
			raise ParameterException(err=f"row [{i}] error: _from/_from_uuid and _to/_to_uuid are null.")

		if (row.from_id != None and row.from_id != "") and (row.to_id is None or row.to_id == ""):
			raise ParameterException(err=f"row [{i}] error: _from has value [{row.from_id}] but _to got null.")

		if (row.from_id is None or row.from_id == "") and (row.to_id != None and row.to_id != ""):
			raise ParameterException(err=f"row [{i}] error: _to has value [{row.to_id}] but _from got null.")

		if row.from_uuid is None and row.to_uuid != None:
			raise ParameterException(
				err=f"row [{i}] error: _to_uuid has value [{row.to_uuid}] but _from_uuid got null.")

		if row.from_uuid != None and row.to_uuid is None:
			raise ParameterException(
				err=f"row [{i}] error: _from_uuid has value [{row.from_uuid}] but _to_uuid got null.")

		for proper in schema.properties:
			if proper.isIdType() or proper.isIgnore():
				continue
			if proper.name not in row.values:
				raise ParameterException(
					err=f"edge row [{i}] error: values doesn't contain property [{proper.name}].")

	@staticmethod
	def checkEntityNodeRow(i: int, schema: ULTIPA_REQUEST.Schema, row: ULTIPA.EntityRow):
		if row._index != None:
			i = row._index

		if row is None:
			raise ParameterException(err=f"The row [{i}] data is null")

		if row.values is None:
			raise ParameterException(err=f"node row [{i}] error: values are empty but  properties size > 0.")

		if not schema.properties and row.values:
			raise ParameterException(err=f"node row [{i}] error: properties are empty but values size > 0.")

		if len(row.values.keys()) > len(schema.properties):
			raise ParameterException(err=f"node row [{i}] error: values size larger than properties size.")

		if len(row.values.keys()) < len(schema.properties):
			raise ParameterException(err=f"node row [{i}] error: values size smaller than properties size.")

		for proper in schema.properties:
			if proper.isIdType() or proper.isIgnore():
				continue
			if proper.name not in row.values:
				raise ParameterException(
					err=f"node row [{i}] error: values doesn't contain property [{proper.name}].")

	@staticmethod
	def checkEntityEdgeRow(i: int, schema: ULTIPA_REQUEST.Schema, row: ULTIPA.EntityRow):
		if row._index != None:
			i = row._index

		if row is None:
			raise ParameterException(err=f"The row [{i}] data is null")
		if row.values is None:
			raise ParameterException(err=f"edge row [{i}] error: values are empty but properties size > 0.")
		if not schema.properties and row.values:
			raise ParameterException(err=f"edge row [{i}] error: properties are empty but values size > 0.")

		if len(row.values.keys()) > len(schema.properties):
			raise ParameterException(err=f"edge row [{i}] error: values size larger than properties size.")

		if len(row.values.keys()) < len(schema.properties):
			raise ParameterException(err=f"edge row [{i}] error: values size smaller than properties size.")

		if ((row.from_id is None or row.from_id == "") and (row.to_id is None or row.to_id == "")) \
				and (row.from_uuid is None and row.to_uuid is None):
			raise ParameterException(err=f"row [{i}] error: _from/_from_uuid and _to/_to_uuid are null.")

		if (row.from_id != None and row.from_id != "") and (row.to_id is None or row.to_id == ""):
			raise ParameterException(err=f"row [{i}] error: _from has value [{row.from_id}] but _to got null.")

		if (row.from_id is None or row.from_id == "") and (row.to_id != None and row.to_id != ""):
			raise ParameterException(err=f"row [{i}] error: _to has value [{row.to_id}] but _from got null.")

		if row.from_uuid is None and row.to_uuid != None:
			raise ParameterException(
				err=f"row [{i}] error: _to_uuid has value [{row.to_uuid}] but _from_uuid got null.")

		if row.from_uuid != None and row.to_uuid is None:
			raise ParameterException(
				err=f"row [{i}] error: _from_uuid has value [{row.from_uuid}] but _to_uuid got null.")

		for proper in schema.properties:
			if proper.isIdType() or proper.isIgnore():
				continue
			if proper.name not in row.values:
				raise ParameterException(
					err=f"edge row [{i}] error: values doesn't contain property [{proper.name}].")

	@staticmethod
	def status(_status, host: str = None) -> ULTIPA.Status:
		statusData = ULTIPA.Status(code=_status.error_code, message=_status.msg)
		isNotRaftMode = _status.error_code == ULTIPA.Code.NOT_RAFT_MODE

		if _status.cluster_info or isNotRaftMode:
			leaderPeer = None
			_followrs = []
			if _status.cluster_info.leader_address or host:
				leaderPeer = ULTIPA.RaftPeerInfo(_status.cluster_info.leader_address or host, True, True, False, False,
												 False)
				leaderPeer.isAlgoExecutable = isNotRaftMode or False
				_followrs.append(leaderPeer)
			for foll in _status.cluster_info.followers:
				status = foll.status == 1
				peer = ULTIPA.RaftPeerInfo(foll.address)
				peer.status = status
				peer.isLeader = False
				peer.isAlgoExecutable = False
				peer.isFollowerReadable = False
				if status:
					peer.isAlgoExecutable = foll.role & ULTIPA.FollowerRole.ROLE_ALGO_EXECUTABLE and True or False
					peer.isFollowerReadable = foll.role & ULTIPA.FollowerRole.ROLE_READABLE and True or False
				peer.isUnset = foll.role == ULTIPA.FollowerRole.ROLE_UNSET
				_followrs.append(peer)
			clusterInfo = ULTIPA.ClusterInfo(_status.cluster_info.redirect, _followrs, leader=leaderPeer)
			statusData.clusterInfo = clusterInfo
		return statusData

	@staticmethod
	def getRaftStatus(data: dict) -> ULTIPA.Status:
		statusData = ULTIPA.Status(code=data.get("code"), message=data.get("message"))
		clusterInfo = ULTIPA.ClusterInfo(redirect=data.get("redirectHost"), raftPeers=data.get("followersPeerInfos"),
										 leader=data.get("leaderInfos"))
		statusData.clusterInfo = clusterInfo
		return statusData

	@staticmethod
	def table(_table, timeZone, timeZoneOffset) -> ULTIPA.Table:
		table_name = _table.table_name
		headers = []
		for h in _table.headers:
			headers.append(h)
		values = []
		for index, row in enumerate(_table.table_rows):
			_vs = []
			for index2, _v in enumerate(row.values):
				if len(headers) > 0:
					property_type = headers[index2].property_type
				else:
					property_type = ULTIPA.PropertyType.PROPERTY_STRING
				_seria = _Serialize(type=property_type, value=_v, timeZone=timeZone, timeZoneOffset=timeZoneOffset)
				unret = _seria.unserialize()
				_vs.append(unret)
			values.append(_vs)
		tableData = ULTIPA.Table(table_name=table_name, headers=headers, table_rows=values)
		return tableData

	@staticmethod
	def tables(_tables, timeZone, timeZoneOffset) -> List[ULTIPA.Table]:
		tablesData = []
		if _tables:
			for table in _tables:
				tableData = FormatType.table(table, timeZone, timeZoneOffset)
				tret = FormatResponse.resTableToArray(table=tableData)
				tablesData.append(tret)
		return tablesData

	@staticmethod
	def statistics(_table, timeZone, timeZoneOffset) -> ULTIPA.UltipaStatistics:
		if not _table:
			return None
		tableData = FormatType.table(_table, timeZone, timeZoneOffset)
		tret = FormatResponse.formatStatisticsTable(table=tableData)
		return tret

	@staticmethod
	def nodeTable(nodeTableData, timeZone, timeZoneOffset):
		SchemaTypeDict = {}
		SchemaHeaderDict = {}
		SchemaSubTypeHeaderDict = {}
		tables = []
		for header in nodeTableData.node_table.schemas:
			schemaName = header.schema_name
			typesDict = {}
			headerDict = {}
			subTypesDict = {}
			for index, header in enumerate(header.properties):
				typesDict.update({index: header.property_type})
				headerDict.update({index: header.property_name})
				subTypesDict.update({index: header.sub_types})

			SchemaTypeDict.update({schemaName: typesDict})
			SchemaHeaderDict.update({schemaName: headerDict})
			SchemaSubTypeHeaderDict.update({schemaName: subTypesDict})

		schemaTypeGet = SchemaTypeDict.get
		schemaHeaderGet = SchemaHeaderDict.get
		schemaSubTypeGet = SchemaSubTypeHeaderDict.get

		for node_row in nodeTableData.node_table.entity_rows:
			if node_row.is_null is True:
				tables.append(None)
				continue
			data = {}
			_id = node_row.id
			uuid = node_row.uuid

			schema_name = node_row.schema_name
			if node_row.values:
				for index, uvalue in enumerate(node_row.values):
					seria = _Serialize(type=schemaTypeGet(schema_name).get(index), value=uvalue,
									   subTypes=schemaSubTypeGet(schema_name).get(index), timeZone=timeZone,
									   timeZoneOffset=timeZoneOffset)
					value = seria.unserialize()
					data.update({schemaHeaderGet(schema_name).get(index): value})
			node = ULTIPA.Node(id=_id, values=data, schema_name=schema_name, uuid=uuid)
			tables.append(node)
		return tables

	@staticmethod
	def edgeTable(edgeTableData, timeZone, timeZoneOffset):
		SchemaTypeDict = {}
		SchemaHeaderDict = {}
		SchemaSubTypeHeaderDict = {}
		tables = []
		for header in edgeTableData.edge_table.schemas:
			schemaName = header.schema_name
			typesDict = {}
			headerDict = {}
			subTypesDict = {}
			for index, header in enumerate(header.properties):
				typesDict.update({index: header.property_type})
				headerDict.update({index: header.property_name})
				subTypesDict.update({index: header.sub_types})

			SchemaTypeDict.update({schemaName: typesDict})
			SchemaHeaderDict.update({schemaName: headerDict})
			SchemaSubTypeHeaderDict.update({schemaName: subTypesDict})

		schemaTypeGet = SchemaTypeDict.get
		schemaHeaderGet = SchemaHeaderDict.get
		schemaSubTypeGet = SchemaSubTypeHeaderDict.get

		for edge_row in edgeTableData.edge_table.entity_rows:
			if edge_row.is_null is True:
				tables.append(None)
				continue
			data = {}
			_from_uuid = edge_row.from_uuid
			_from_id = edge_row.from_id
			_to_uuid = edge_row.to_uuid
			_to_id = edge_row.to_id
			schema_name = edge_row.schema_name
			uuid = edge_row.uuid
			if edge_row.values:
				for index, uvalue in enumerate(edge_row.values):
					seria = _Serialize(type=schemaTypeGet(schema_name).get(index), value=uvalue,
									   subTypes=schemaSubTypeGet(schema_name).get(index), timeZone=timeZone,
									   timeZoneOffset=timeZoneOffset)
					value = seria.unserialize()
					data.update({schemaHeaderGet(schema_name).get(index): value})
			edge = ULTIPA.Edge(from_id=_from_id, to_id=_to_id, values=data, uuid=uuid, from_uuid=_from_uuid,
							   to_uuid=_to_uuid, schema_name=schema_name)
			tables.append(edge)
		return tables

	@staticmethod
	def attrEntity(entityRows, type: str):
		entityList = []
		for data in entityRows.entity_rows:
			if type == "node":
				entityList.append(ULTIPA.Node(values=None, uuid=data.uuid))
			else:
				entityList.append(ULTIPA.Edge(values=None, uuid=data.uuid))
		return entityList

	@staticmethod
	def propertyType(type: str) -> ULTIPA.PropertyType:
		'''
		Convert the type input by the user to ULTIPA.PropertyType
		:param type:
		:return:
		'''
		if type.upper() == 'PROPERTY_STRING' or type.upper() == 'STRING':
			type = ULTIPA.PropertyType.PROPERTY_STRING
		elif type.upper() == 'PROPERTY_INT32' or type.upper() == 'INT32':
			type = ULTIPA.PropertyType.PROPERTY_INT32
		elif type.upper() == 'PROPERTY_INT64' or type.upper() == 'INT64':
			type = ULTIPA.PropertyType.PROPERTY_INT64
		elif type.upper() == 'PROPERTY_FLOAT' or type.upper() == 'FLOAT':
			type = ULTIPA.PropertyType.PROPERTY_FLOAT
		elif type.upper() == 'PROPERTY_DOUBLE' or type.upper() == 'DOUBLE':
			type = ULTIPA.PropertyType.PROPERTY_DOUBLE
		elif type.upper() == 'PROPERTY_UINT32' or type.upper() == 'UINT32':
			type = ULTIPA.PropertyType.PROPERTY_UINT32
		elif type.upper() == 'PROPERTY_UINT64' or type.upper() == 'UINT64':
			type = ULTIPA.PropertyType.PROPERTY_UINT64
		elif type.upper() == 'PROPERTY_DATETIME' or type.upper() == 'DATETIME':
			type = ULTIPA.PropertyType.PROPERTY_DATETIME
		elif type.upper() == 'PROPERTY_TIMESTAMP' or type.upper() == 'TIMESTAMP':
			type = ULTIPA.PropertyType.PROPERTY_TIMESTAMP
		elif type.upper() == 'PROPERTY_TEXT' or type.upper() == 'TEXT':
			type = ULTIPA.PropertyType.PROPERTY_TEXT
		elif type.upper() == 'PROPERTY_UUID' or type.upper() == 'UUID':
			type = ULTIPA.PropertyType.PROPERTY_UUID
		elif type.upper() == 'PROPERTY_ID' or type.upper() == 'ID':
			type = ULTIPA.PropertyType.PROPERTY_ID
		elif type.upper() == 'PROPERTY_FROM' or type.upper() == 'FROM':
			type = ULTIPA.PropertyType.PROPERTY_FROM
		elif type.upper() == 'PROPERTY_FROM_UUID' or type.upper() == 'FROM_UUID':
			type = ULTIPA.PropertyType.PROPERTY_FROM_UUID
		elif type.upper() == 'PROPERTY_TO' or type.upper() == 'TO':
			type = ULTIPA.PropertyType.PROPERTY_TO
		elif type.upper() == 'PROPERTY_TO_UUID' or type.upper() == 'TO_UUID':
			type = ULTIPA.PropertyType.PROPERTY_TO_UUID
		elif type.upper() == 'PROPERTY_IGNORE' or type.upper() == 'IGNORE':
			type = ULTIPA.PropertyType.PROPERTY_IGNORE

		return type

	@staticmethod
	def _formatTableHeader(headers):
		headerList = []
		headertype = {}
		if isinstance(headers, str):
			headers = json.loads(headers)
		if isinstance(headers, list) and isinstance(headers, list):
			for index, header in enumerate(headers):
				headdic = {}
				if isinstance(header, dict):
					type = FormatType.propertyType(header.get('type'))
					headdic.update({'property_name': header.get('name')})
					headdic.update({'property_type': type})
					headertype.update({header.get('name'): type})
					headerList.append(headdic)
				else:
					headdic.update({'property_name': header.name})
					headdic.update({'property_type': header.type})
					if header.name in headertype:
						headertype.update({header.name: header.type})
						headerList.append(headdic)
					else:
						raise ParameterException('Attribute names cannot be the same')
		else:
			raise ParameterException(err='The headers and rows must be list')

		return (headerList, headertype)

	@staticmethod
	def pathScheams(path):
		nodeSchemas = {}
		edgeSchemas = {}
		for header in path.node_table.schemas:
			schemaName = header.schema_name
			propetyList = []
			for index, property in enumerate(header.properties):
				subTypes = [Property._getStringByPropertyType(sbt) for sbt in property.sub_types]
				newproperty = ULTIPA.Property(property.property_name,subTypes=subTypes)
				newproperty.type = Property._getStringByPropertyType(property.property_type)
				propetyList.append(newproperty)
			nodeSchemas.update({schemaName: ULTIPA.Schema(schemaName,None,None,None, propetyList, None)})
		for header in path.edge_table.schemas:
			schemaName = header.schema_name
			propetyList = []
			for index, property in enumerate(header.properties):
				subTypes = [Property._getStringByPropertyType(sbt) for sbt in property.sub_types]
				newproperty = ULTIPA.Property(property.property_name,subTypes=subTypes)
				newproperty.type = Property._getStringByPropertyType(property.property_type)
				propetyList.append(newproperty)
			edgeSchemas.update({schemaName: ULTIPA.Schema(schemaName,None,None,None, propetyList, None)})
		return nodeSchemas, edgeSchemas

	@staticmethod
	def makeEntityNodeTable(schema: ULTIPA_REQUEST.Schema, entity_rows: List[ULTIPA.EntityRow],
							timeZoneOffset=None) -> ULTIPA.NodeEntityTable:

		nodetable = ULTIPA.NodeEntityTable([], [])
		nodetable.schemas.append({"schema_name": schema.name, "properties": []})

		for prop in schema.properties:
			if prop.isIdType() or prop.isIgnore():
				continue
			nodetable.schemas[0].get("properties").append(
				{"property_name": prop.name, "property_type": prop.type, "sub_types": prop.subTypes})
		for i, row in enumerate(entity_rows):
			append = True
			values = []
			FormatType.checkEntityNodeRow(i, schema, row)
			for proper in schema.properties:
				if proper.isIdType() or proper.isIgnore():
					continue
				if proper.name in row.values:
					value = row.values.get(proper.name)
					if isinstance(proper.type,str):
						ptype = proper.getPropertyTypeByString(proper.type)
					else:
						ptype = proper.type
					checkRet = TypeCheck.checkProperty(ptype, value)
					if isinstance(checkRet, bool):
						try:
							_seria = _Serialize(type=ptype, value=value, name=proper.name,
												timeZoneOffset=timeZoneOffset, subTypes=proper.subTypes)
							sdata = _seria.serialize()
							values.append(sdata)
						except Exception as e:
							if len(e.args) > 0 and "%s" in e.args[0]:
								e = e.args[0] % (proper.name, value)
							raise ParameterException(err=f"node row [{row._getIndex()}] error: {e}")

					else:
						raise ParameterException(
							err=checkRet % ("node", row._getIndex(), proper.name, value))
				else:
					raise ParameterException(
						err=f"node row [{row._getIndex()}] error: values doesn't contain property [{proper.name}].")
			if append:
				data = {"schema_name": schema.name, "values": values}
				if row.uuid:
					data.update({"uuid": row.uuid})
				if row.id:
					data.update({"id": row.id})

				nodetable.nodeRows.append(data)
		return nodetable

	@staticmethod
	def makeEntityEdgeTable(schema: ULTIPA_REQUEST.Schema, rows: List[ULTIPA.EntityRow],
							timeZoneOffset=None) -> ULTIPA.EdgeEntityTable:
		edgetable = ULTIPA.EdgeEntityTable([], [])
		edgetable.schemas.append({"schema_name": schema.name, "properties": []})
		for prop in schema.properties:
			if prop.isIdType() or prop.isIgnore():
				continue
			edgetable.schemas[0].get("properties").append({"property_name": prop.name, "property_type": prop.type})
		for i, row in enumerate(rows):
			append = True
			values = []
			FormatType.checkEntityEdgeRow(i, schema, row)
			for proper in schema.properties:
				if proper.isIdType() or proper.isIgnore():
					continue
				if proper.name in row.values:
					value = row.values.get(proper.name)
					if isinstance(proper.type, str):
						ptype = proper.getPropertyTypeByString(proper.type)
					else:
						ptype = proper.type
					checkRet = TypeCheck.checkProperty(ptype, value)
					if isinstance(checkRet, bool):
						try:
							_seria = _Serialize(type=ptype, value=value, name=proper.name, subTypes=proper.subTypes,
												timeZoneOffset=timeZoneOffset)
							sdata = _seria.serialize()
							values.append(sdata)
						except Exception as e:
							raise ParameterException(err=f"edge row [{row._getIndex()}] error:{e}.")
					else:
						raise ParameterException(
							err=checkRet % ("edge", row._getIndex(), proper.name, value))
				else:
					raise ParameterException(
						err=f"edge row [{row._getIndex()}] error: values doesn't contain property [{proper.name}].")

			if append:
				data = {"schema_name": schema.name, "values": values}
				if row.from_uuid:
					data.update({"from_uuid": row.from_uuid})
				if row.to_uuid:
					data.update({"to_uuid": row.to_uuid})
				if row.from_id:
					data.update({"from_id": row.from_id})
				if row.to_id:
					data.update({"to_id": row.to_id})
				if row.uuid:
					data.update({"uuid": row.uuid})
				edgetable.edgeRows.append(data)
		return edgetable

	@staticmethod
	def nodeAliases(_nodes, timeZone, timeZoneOffset) -> List[ULTIPA.NodeAlias]:
		nodeAliasesData = []
		if _nodes:
			for node in _nodes:
				nodesData = FormatType.nodeTable(node, timeZone, timeZoneOffset)
				nodeAliasData = ULTIPA.NodeAlias(alias=node.alias, nodes=nodesData)
				nodeAliasesData.append(nodeAliasData)
		return nodeAliasesData

	@staticmethod
	def graph(graph, timeZone, timeZoneOffset) -> ULTIPA.Graph:
		if graph:
			nodeTable = FormatType.nodeTable(graph, timeZone, timeZoneOffset)
			edgeTable = FormatType.edgeTable(graph, timeZone, timeZoneOffset)
			return ULTIPA.Graph(nodeTable,edgeTable)
		return ULTIPA.Graph(None,None)


	@staticmethod
	def graphAlias(graphs,timeZone, timeZoneOffset) -> List[ULTIPA.GraphAlias]:
		nodeAliasesData = []
		if graphs:
			for graph in graphs:
				graphData = FormatType.graph(graph.graph, timeZone, timeZoneOffset)
				nodeAliasData = ULTIPA.GraphAlias(alias=graph.alias,graph=graphData)
				nodeAliasesData.append(nodeAliasData)
		return nodeAliasesData




	@staticmethod
	def attrNodeEntityTable(data) -> List[ULTIPA.Node]:
		return FormatType.attrEntity(data, "node")

	@staticmethod
	def attrEdgeEntityTable(data) -> List[ULTIPA.Edge]:
		return FormatType.attrEntity(data, "edge")

	@staticmethod
	def edgeAliases(_edges, timeZone, timeZoneOffset) -> List[ULTIPA.EdgeAlias]:
		edgeAliasesData = []
		if _edges:
			for edge in _edges:
				edgesData = FormatType.edgeTable(edge, timeZone, timeZoneOffset)
				edgeAliasData = ULTIPA.EdgeAlias(alias=edge.alias, edges=edgesData)
				edgeAliasesData.append(edgeAliasData)
		return edgeAliasesData

	@staticmethod
	def values(_values) -> 'dict':
		value_dict = {}
		if _values:
			for value in _values:
				value_dict.update({value.key: value.value})
		return value_dict

	@classmethod
	def parseAttrListData(cls, datas) -> List[ULTIPA.PaserAttrListData]:
		PaserAttrRetList = []
		for data in datas:
			attrListRet = []
			pathListRet = []
			nodetRet = None
			edgeRet = None
			attrListData = AttrListData()
			attrListData.ParseFromString(data)
			if attrListData.type == ULTIPA.ResultType.RESULT_TYPE_ATTR:
				for attr in attrListData.attrs:
					attrListRet.append(cls.parseAttr(attr, None))

			if attrListData.type == ULTIPA.ResultType.RESULT_TYPE_PATH:
				pathListRet.extend(FormatType.attrPath(attrListData.paths, None, None))

			if attrListData.type == ULTIPA.ResultType.RESULT_TYPE_NODE:
				nodetRet = FormatType.attrNodeEntityTable(attrListData.nodes)

			if attrListData.type == ULTIPA.ResultType.RESULT_TYPE_EDGE:
				edgeRet = FormatType.attrEdgeEntityTable(attrListData.edges)

			PaserAttrRetList.append(
				ULTIPA.PaserAttrListData(attrListData.type, nodes=nodetRet, edges=edgeRet, paths=pathListRet,
										 attrs=attrListRet))
		return PaserAttrRetList

	@classmethod
	def parseAttr(cls, attr, aliasName) -> ULTIPA.Attr:
		valuesList = []
		attr_type = attr.value_type
		if attr_type == ULTIPA.PropertyType.PROPERTY_LIST:
			valuesList = FormatType.parseAttrListData(attr.values)
			return ULTIPA.Attr(alias=aliasName, values=valuesList,
									type=Property._getStringByPropertyType(attr_type))

		for att in attr.values:
			_seria = _Serialize(type=attr_type, value=att)
			sdata = _seria.unserialize()
			valuesList.append(sdata)
		return ULTIPA.Attr(alias=aliasName, values=valuesList,
								type=Property._getStringByPropertyType(attr_type))

	@classmethod
	def parseAttrAlias(cls, attrAlias) -> ULTIPA.Attr:
		return cls.parseAttr(attrAlias.attr, attrAlias.alias)

	@staticmethod
	def attrAlias1(_attrs) -> List[ULTIPA.Attr]:
		attr_list = []
		if _attrs:
			for attr in _attrs:
				attr_list.append(FormatType.parseAttrAlias(attr))
		return attr_list

	@staticmethod
	def attr(attr, timeZone, timeZoneOffset) -> ULTIPA.UltipaAttr:
		type = attr.value_type
		result = ULTIPA.UltipaAttr(type, None, has_attr_data=False, has_ultipa_data=False,
							 type_desc=Property._getStringByPropertyType(type))
		result.values = []
		for value in attr.values:
			if type == ULTIPA.PropertyType.PROPERTY_NULL:
				result.has_attr_data = True
				result.values.append(None)
				continue
			if type == ULTIPA.PropertyType.PROPERTY_LIST or type== ULTIPA.PropertyType.PROPERTY_SET:
				attrListData = AttrListData()
				attrListData.ParseFromString(value)
				result_type: any = attrListData.type
				if attrListData.is_null:
					result.values.append(None)
					continue

				if result_type == ULTIPA.ResultType.RESULT_TYPE_ATTR:
					attrs = []
					for attr in attrListData.attrs:
						att = FormatType.attr(attr, timeZone, timeZoneOffset)
						if not att.values:
							attrs.append(att.values)
						else:
							attrs.extend(att.values)
					if len(attrs) != 0:
						result.has_attr_data = True
					result.values.append(attrs)

				if result_type == ULTIPA.ResultType.RESULT_TYPE_PATH:
					result.has_ultipa_data = True
					result.values.append(ULTIPA.PaserAttrListData(attrListData.type,
																  paths=FormatType.attrPath(attrListData.paths,
																							timeZone, timeZoneOffset)))

				if result_type == ULTIPA.ResultType.RESULT_TYPE_NODE:
					result.has_ultipa_data = True
					result.values.append(ULTIPA.PaserAttrListData(attrListData.type,
																  nodes=FormatType.attrNodeEntityTable(
																	  attrListData.nodes)))

				if result_type == ULTIPA.ResultType.RESULT_TYPE_EDGE:
					result.has_ultipa_data = True
					result.values.append(ULTIPA.PaserAttrListData(attrListData.type,
																  edges=FormatType.attrEdgeEntityTable(
																	  attrListData.edges)))
			else:
				_seria = _Serialize(type=type, value=value, timeZone=timeZone, timeZoneOffset=timeZoneOffset)
				sdata = _seria.unserialize()
				result.has_attr_data = True
				result.values.append(sdata)
		return result

	@staticmethod
	def attrAlias(_attrs, timeZone, timeZoneOffset) -> List[ULTIPA.AttrNewAlias]:
		attr_list = []
		if _attrs:
			for attr in _attrs:
				attr_data = FormatType.attr(attr.attr, timeZone, timeZoneOffset)
				attr_list.append(ULTIPA.AttrNewAlias(alias=attr.alias, attr=attr_data))
		return attr_list

	@staticmethod
	def arrays(_arrays) -> List[ULTIPA.ArrayAlias]:
		arrays_list = []
		if _arrays:
			for attr in _arrays:
				li = []
				attr_type = attr.property_type
				for att in attr.elements:
					value_li = []
					for el in att.values:
						_seria = _Serialize(type=attr_type, value=el)
						sdata = _seria.unserialize()
						value_li.append(sdata)
					li.append(value_li)
				ret = ULTIPA.ArrayAlias(alias=attr.alias, elements=li)
				arrays_list.append(ret)
		return arrays_list

	@staticmethod
	def resultalias(_arrays) -> List[ULTIPA.ResultAlias]:
		value_dict = []
		if _arrays:
			for value in _arrays:
				value_dict.append(ULTIPA.ResultAlias(value.alias, ResultType.getTypeStr(value.result_type)))	
		return value_dict

	@staticmethod
	def explainPlan(_explainPlan) -> List[ULTIPA.ExplainPlan]:
		explainPlanRet = []
		if _explainPlan:
			for value in _explainPlan.plan_nodes:
				explainPlanRet.append(
					ULTIPA.ExplainPlan(value.alias, value.children_num, value.uql, value.infos))
		return explainPlanRet
	@staticmethod
	def export_edges(_edges, timeZone, timeZoneOffset) -> List:
		edgeTableData = FormatType.edgeTable(_edges, timeZone, timeZoneOffset)

		return edgeTableData

	@staticmethod
	def export_nodes(_nodes, timeZone, timeZoneOffset) -> List:
		nodeTableData = FormatType.nodeTable(_nodes, timeZone, timeZoneOffset)
		return nodeTableData


	@staticmethod
	def pathAlias(_paths, timeZone, timeZoneOffset) -> [ULTIPA.PathAlias]:
		pathData = []
		if _paths:
			for path in _paths:
				pathAlia = ULTIPA.PathAlias(path.alias)
				for npath in path.paths:
					nodeAliasesData = FormatType.nodeTable(npath, timeZone, timeZoneOffset)
					edgeAliasesData = FormatType.edgeTable(npath, timeZone, timeZoneOffset)
					nodeSchema, edgeSchema = FormatType.pathScheams(npath)
					newPath = ULTIPA.Path(nodes=nodeAliasesData, edges=edgeAliasesData, nodeSchemas=nodeSchema,
										  edgeSchemas=edgeSchema)
					pathAlia.paths.append(newPath)
				pathData.append(pathAlia)
		return pathData

	@staticmethod
	def attrPath(_paths, timeZone, timeZoneOffset) -> [ULTIPA.Path]:
		pathData = []
		if _paths:
			for path in _paths:
				nodeAliasesData = FormatType.nodeTable(path, timeZone, timeZoneOffset)
				edgeAliasesData = FormatType.edgeTable(path, timeZone, timeZoneOffset)
				nodeSchema, edgeSchema = FormatType.pathScheams(path)
				newPath = ULTIPA.Path(nodes=nodeAliasesData, edges=edgeAliasesData, nodeSchemas=nodeSchema,
									  edgeSchemas=edgeSchema)
				pathData.append(newPath)
		return pathData

	@staticmethod
	def Response(_res, host: str = None) -> ULTIPA_RESPONSE.Response:
		status = FormatType.status(_res.status, host)
		res = ULTIPA_RESPONSE.Response(status)
		return res

	@staticmethod
	def mergeUqlResponse(mergeRes: ULTIPA_RESPONSE.Response, res: ULTIPA_RESPONSE.Response):
		if not mergeRes.data:
			mergeRes = copy.deepcopy(res)
			return mergeRes
		if res.data.paths:
			mergeRes.data.paths = DataMerge.concat(mergeRes.data.paths, res.data.paths)
		if res.data.nodes:
			mergeRes.data.nodes = DataMerge.concat(mergeRes.data.nodes, res.data.nodes, 'nodes')
		if res.data.edges:
			mergeRes.data.edges = DataMerge.concat(mergeRes.data.edges, res.data.edges, 'edges')
		if res.data.attrs:
			mergeRes.data.attrs = DataMerge.concat(mergeRes.data.attrs, res.data.attrs, 'values')
		if res.data.tables:
			mergeRes.data.tables = DataMerge.concat(mergeRes.data.tables, res.data.tables, "table_name", ["headers"])
		if res.data.explainPlan:
			mergeRes.data.explainPlan = DataMerge.concat(mergeRes.data.explainPlan, res.data.explainPlan)
		if res.data.resultAlias:
			mergeRes.data.resultAlias = DataMerge.concat(mergeRes.data.resultAlias, res.data.resultAlias)
		if res.statistics:
			mergeRes.statistics = DataMerge.concat(mergeRes.statistics, res.statistics)

		return mergeRes

	@staticmethod
	def response(uql_response: ULTIPA_RESPONSE.Response, uqlReply, timeZone,
				 timeZoneOffset) -> ULTIPA_RESPONSE.Response:
		attrs = FormatType.attrAlias(uqlReply.attrs, timeZone, timeZoneOffset)		
		attrs_attrs = []
		attrs_map = {}

		def addAttributes(alias: str, type: ULTIPA.ResultType, values: any, dataMap: HasDataMap) -> None:
			if attrs_map.get(alias) is None:
				if dataMap.has_attr_data:
					type = ULTIPA.ResultType.RESULT_TYPE_ATTR
				attralias = ULTIPA.Attr(alias=alias, type=type, type_desc=ULTIPA.ResultType.getTypeStr(type),
											 values=[])
				attrs_map[alias] = attralias
				attrs_attrs.append(attralias)
			if type == ULTIPA.ResultType.RESULT_TYPE_ATTR and dataMap.only_attr_list:
				attrs_map[alias].values = values
			else:
				attrs_map[alias].values.append(values)

		for attrAlias in attrs:
			alias = attrAlias.alias
			has_attr_data = attrAlias.attr.has_attr_data
			has_ultipa_data = attrAlias.attr.has_ultipa_data
			only_attr_list = has_attr_data and not has_ultipa_data
			dataMap = HasDataMap(has_ultipa_data=has_ultipa_data, has_attr_data=has_attr_data,
								 only_attr_list=only_attr_list)
			if attrAlias.attr.type == ULTIPA.PropertyType.PROPERTY_LIST:
				if only_attr_list:
					addAttributes(alias, ULTIPA.ResultType.RESULT_TYPE_ATTR, attrAlias.attr.values, dataMap)
					continue

				for row in attrAlias.attr.values:
					if not row or not row.type:
						addAttributes(alias, ULTIPA.ResultType.RESULT_TYPE_ATTR, row, dataMap)
						continue

					if not isinstance(row, ULTIPA.PaserAttrListData):
						addAttributes(alias, ULTIPA.ResultType.RESULT_TYPE_ATTR, row, dataMap)
						continue

					if row.type == ULTIPA.ResultType.RESULT_TYPE_NODE:
						addAttributes(alias, row.type, row.nodes, dataMap)

					elif row.type == ULTIPA.ResultType.RESULT_TYPE_EDGE:
						addAttributes(alias, row.type, row.edges, dataMap)

					elif row.type == ULTIPA.ResultType.RESULT_TYPE_PATH:
						addAttributes(alias, row.type, row.paths, dataMap)

			else:
				addAttributes(alias, ULTIPA.ResultType.RESULT_TYPE_ATTR, attrAlias.attr.values, dataMap)

		status = FormatType.status(uqlReply.status)
		tables = FormatType.tables(uqlReply.tables, timeZone, timeZoneOffset)
		paths = FormatType.pathAlias(uqlReply.paths, timeZone, timeZoneOffset)
		graphs = FormatType.graphAlias(uqlReply.graphs, timeZone, timeZoneOffset)
		nodes = FormatType.nodeAliases(uqlReply.nodes, timeZone, timeZoneOffset)  # ForamtType.nodeAliases
		edges = FormatType.edgeAliases(uqlReply.edges, timeZone, timeZoneOffset)
		attrs = attrs_attrs
		statistics = FormatType.statistics(uqlReply.statistics, timeZone, timeZoneOffset)
		resultAlias = FormatType.resultalias(uqlReply.alias)
		explainPlan = FormatType.explainPlan(uqlReply.explain_plan)
		baseReply = ULTIPA.BaseUqlReply(paths=paths, nodes=nodes, edges=edges, tables=tables,
										attrs=attrs, resultAlias=resultAlias, explainPlan=explainPlan,graphs=graphs)
		uql_response.status = status
		uql_response.statistics = statistics
		uql_response.data = baseReply
		uql_response.aliases = resultAlias
		return uql_response

	@staticmethod
	def uqlResponse(_res, timeZone, timeZoneOffset) -> ULTIPA_RESPONSE.UltipaResponse:
		uql_response = ULTIPA_RESPONSE.Response()
		ultipa_response = ULTIPA_RESPONSE.UltipaResponse()
		for uqlReply in _res:
			status = FormatType.status(uqlReply.status)
			uql_response = FormatType.response(uql_response, uqlReply, timeZone, timeZoneOffset)
			ret = ULTIPA.UqlReply(dataBase=uql_response.data)

			if status.code != ULTIPA.Code.SUCCESS:
				ultipa_response.status = uql_response.status
				ultipa_response.req = uql_response.req
				return ultipa_response

			ultipa_response.items = ret._aliasMap
			ultipa_response.status = uql_response.status
			ultipa_response.req = uql_response.req
			ultipa_response.statistics = uql_response.statistics
			yield ultipa_response

	@staticmethod
	def uqlMergeResponse(_res, timeZone, timeZoneOffset) -> ULTIPA_RESPONSE.UltipaResponse:
		uql_response = ULTIPA_RESPONSE.Response()
		mergeRes = ULTIPA_RESPONSE.Response()
		ultipa_response = ULTIPA_RESPONSE.UltipaResponse()
		aliasvalue=[]
		for uqlReply in _res:
			status = FormatType.status(uqlReply.status)
			uql_response = FormatType.response(uql_response, uqlReply, timeZone, timeZoneOffset)
			if uql_response.aliases:
				aliasvalue.append(uql_response.aliases)
			if status.code != ULTIPA.Code.SUCCESS:
				ultipa_response.status = uql_response.status
				ultipa_response.req = uql_response.req
				return ultipa_response
			mergeRes = FormatType.mergeUqlResponse(mergeRes, uql_response)

		ret = ULTIPA.UqlReply(dataBase=mergeRes.data)
		ultipa_response.items = ret._aliasMap
		ultipa_response.explainPlan = ret.explainPlan
		ultipa_response.status = uql_response.status
		ultipa_response.req = uql_response.req
		if len(aliasvalue)>0:
			ultipa_response.aliases = aliasvalue[0]
		else:	
			ultipa_response.aliases = uql_response.aliases
		# ultipa_response.aliases = uql_response.aliases
		# ultipa_response.aliases = aliasvalue[0]
		ultipa_response.statistics = uql_response.statistics
		return ultipa_response

	@staticmethod
	def downloadResponse(_res) -> ULTIPA_RESPONSE.Response:
		for uqlReply in _res:
			status = FormatType.status(uqlReply.status)
			data = FormatType.status(uqlReply.chunk)
			total_time = uqlReply.total_time_cost
			engine_time = uqlReply.total_time_cost
			res = ULTIPA_RESPONSE.Response(status, total_time, engine_time, data)
			return res

	@staticmethod
	def exportResponse(_res, timeZone, timeZoneOffset) -> ULTIPA_RESPONSE.Response:
		nodedata = []
		edgedata = []
		res = ULTIPA_RESPONSE.Response()
		for uqlReply in _res:
			res.status = FormatType.status(uqlReply.status)
			if uqlReply.node_table:
				nodedata = FormatType.export_nodes(uqlReply, timeZone, timeZoneOffset)
			if uqlReply.edge_table:
				edgedata = FormatType.export_edges(uqlReply, timeZone, timeZoneOffset)
			if nodedata:
				uql = ULTIPA.ExportReply(data=nodedata)
				res.data = uql.data
			if edgedata:
				uql = ULTIPA.ExportReply(data=edgedata)
				res.data = uql.data
			break
		return res

	@staticmethod
	def graphPrivileges(graphPrivileges: '[object]'):
		new_graphPrivileges = []

		if graphPrivileges:
			for gp in graphPrivileges:
				graphDcit = {}
				graphDcit.update({'name': list(gp.keys())[0]})
				graphDcit.update({'values': list(gp.values())[0]})
				new_graphPrivileges.append(graphDcit)

		return new_graphPrivileges

