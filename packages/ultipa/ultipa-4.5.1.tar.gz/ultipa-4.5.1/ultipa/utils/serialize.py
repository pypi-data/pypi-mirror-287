import datetime

from ultipa.proto.ultipa_pb2 import ListData, SetData, AttrListData
from ultipa.structs import Property
from ultipa.types import ULTIPA
from struct import *

from ultipa.utils import nullValue
from ultipa.utils.common import DateTimeIs2Str, Float_Accuracy, TimestampIs2Str
from ultipa.utils.ultipa_datetime import UltipaDatetime
from ultipa.utils.errors import ParameterException, ServerException, SerializeException, checkError


class _Serialize:
	'''
	Configuration class that defines settings for serialization.
	'''
	def __init__(self, type, value, name=None, export=False, timeZoneOffset=None, subTypes=None, timeZone=None):
		self.type = type
		self.value = value
		self.subTypes = subTypes
		self.name = name
		self.export = export
		self.timeZoneOffset = timeZoneOffset
		self.timeZone = timeZone

	def serialize(self):
		if self.value is None and not self.subTypes:
			self.value = nullValue.nullValue(self.type)
			return self.value

		# if self.value is None:
		# 	self.value = nullValue.nullValue(self.type)
		# 	return self.value
		if self.type == ULTIPA.PropertyType.PROPERTY_BLOB:
			return self.value

		if self.type == ULTIPA.PropertyType.PROPERTY_STRING or self.type == ULTIPA.PropertyType.PROPERTY_TEXT or self.type == ULTIPA.PropertyType.PROPERTY_POINT or self.type == ULTIPA.PropertyType.PROPERTY_DECIMAL:
			if isinstance(self.value, str):
				return self.value.encode()
			elif isinstance(self.value, bytes):
				return self.value
			else:
				return str(self.value).encode()

		elif self.type == ULTIPA.PropertyType.PROPERTY_INT32:
			if self.value == '':
				self.value = 0
			try:
				upret = pack('>i', int(self.value))
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")

		elif self.type == ULTIPA.PropertyType.PROPERTY_UINT32:
			if self.value == '':
				self.value = 0
			try:
				upret = pack('>I', int(self.value))
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")

		elif self.type == ULTIPA.PropertyType.PROPERTY_INT64:
			if self.value == '':
				self.value = 0
			try:
				upret = pack('>q', int(self.value))
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")


		elif self.type == ULTIPA.PropertyType.PROPERTY_UINT64:
			if self.value == '':
				self.value = 0
			try:
				upret = pack('>Q', int(self.value))
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")

		elif self.type == ULTIPA.PropertyType.PROPERTY_FLOAT:
			if self.value == '':
				self.value = 0

			try:
				upret = pack('>f', self.value)
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")

		elif self.type == ULTIPA.PropertyType.PROPERTY_DOUBLE:
			if self.value == '':
				self.value = 0
			try:
				upret = pack('>d', self.value)
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")

		elif self.type == ULTIPA.PropertyType.PROPERTY_DATETIME:
			if self.value is None:
				self.value = 0
			else:
				self.value = UltipaDatetime.datetimeStr2datetimeInt(self.value)
			try:
				upret = pack('>Q', self.value)
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")
			return upret

		elif self.type == ULTIPA.PropertyType.PROPERTY_TIMESTAMP:
			if self.value is None:
				self.value = 0
			else:
				if isinstance(self.value, datetime.datetime):
					self.value = int(self.value.timestamp())
				if isinstance(self.value, str):
					self.value = UltipaDatetime.timestampStr2timestampInt(self.value, self.timeZone,
																		  self.timeZoneOffset)
			try:
				upret = pack('>I', self.value)
				return upret
			except Exception as e:
				error = checkError(e.args[0])
				raise SerializeException(err=f"property [%s],value=%s {error}")

		elif (self.type == ULTIPA.PropertyType.PROPERTY_LIST or self.type == ULTIPA.PropertyType.PROPERTY_SET)and self.subTypes != None and len(self.subTypes) > 0:
			listData = ListData()
			if self.value == None:
				listData.is_null = True
				self.value = []
			for i, v in enumerate(self.value):
				if isinstance(self.subTypes[0],str):
					type = Property._getPropertyTypeByString(self.subTypes[0])
				else:
					type = self.subTypes[0]
				listData.values.append(_Serialize(type, v, timeZone=self.timeZone,
										  timeZoneOffset=self.timeZoneOffset).serialize())
			return listData.SerializeToString()


		elif self.type == ULTIPA.PropertyType.PROPERTY_MAP and self.subTypes != None and len(self.subTypes) > 0:
			setData = SetData()
			if self.value == None:
				setData.is_null = True
				self.value = set()
			for i, v in enumerate(self.value):
				setData.values.add(_Serialize(self.subTypes[0], v).serialize())
			return setData.SerializeToString()

	def unserialize(self):
		try:
			if self.type == ULTIPA.PropertyType.PROPERTY_NULL:
				return None

			if nullValue.isNullValue(self.value, self.type):
				return None

			elif self.type == ULTIPA.PropertyType.PROPERTY_BLOB:
				return list(bytearray(self.value))

			elif self.type == ULTIPA.PropertyType.PROPERTY_STRING or self.type == ULTIPA.PropertyType.PROPERTY_DECIMAL or self.type == ULTIPA.PropertyType.PROPERTY_TEXT or self.type == ULTIPA.PropertyType.PROPERTY_POINT or type is None:
				return self.value.decode()

			elif self.type == ULTIPA.PropertyType.PROPERTY_INT32:
				if len(self.value) >= 4:
					ls = len(self.value) // 4 * 'i' or 'i'
				elif len(self.value) == 2:
					ls = len(self.value) // 2 * 'h' or 'h'
				else:
					ls = 'h'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_UINT32:
				ls = len(self.value) // 4 * 'I' or 'I'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_INT64:
				ls = len(self.value) // 8 * 'q' or 'q'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_UINT64:
				ls = len(self.value) // 8 * 'Q' or 'Q'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_FLOAT:
				ls = len(self.value) // 4 * 'f' or 'f'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				if Float_Accuracy:
					return round(ret, 7)
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_DOUBLE:
				ls = len(self.value) // 8 * 'd' or 'd'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_DATETIME:
				ls = len(self.value) // 8 * 'Q' or 'Q'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				if DateTimeIs2Str:
					ret = UltipaDatetime.datetimeInt2datetimeStr(ret)
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_TIMESTAMP:
				ls = len(self.value) // 4 * 'I' or 'I'
				upret = unpack(f'>{ls}', self.value)
				ret = upret[0]
				if TimestampIs2Str:
					ret = UltipaDatetime.timestampInt2timestampStr(ret, self.timeZone, self.timeZoneOffset)
				if nullValue.isNullValue(self.value, self.type):
					return None
				return ret
			elif self.type == ULTIPA.PropertyType.PROPERTY_LIST and self.subTypes != None and len(self.subTypes) > 0:
				ret = []
				listData = ListData()
				listData.ParseFromString(self.value)
				if listData.is_null == True:
					return None
				for v in listData.values:
					ret.append(_Serialize(self.subTypes[0], v, timeZone=self.timeZone,
										  timeZoneOffset=self.timeZoneOffset).unserialize())
				return ret

			elif self.type == ULTIPA.PropertyType.PROPERTY_SET:
				ret = set()
				setData = SetData()
				setData.ParseFromString(self.value)
				if setData.is_null == True:
					return None
				for value in setData.values:
					ret.add(_Serialize(self.subTypes[0], value, timeZone=self.timeZone,
										  timeZoneOffset=self.timeZoneOffset).unserialize())
				return list(ret)
			else:
				raise ServerException('Server returned type error')

		except Exception as e:
			raise ParameterException(err=e)

	def setDefaultValue(self):
		if self.type == ULTIPA.PropertyType.PROPERTY_STRING:
			self.value = ""
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_INT32:
			self.value = 0
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_UINT32:
			self.value = 0
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_INT64:
			self.value = 0
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_UINT64:
			self.value = 0
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_FLOAT:
			self.value = 0
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_DOUBLE:
			self.value = 0
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_TEXT:
			self.value = ""
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_DATETIME:
			self.value = "1970-01-01"
			return
		elif self.type == ULTIPA.PropertyType.PROPERTY_TIMESTAMP:
			self.value = "1970-01-01"
			return
