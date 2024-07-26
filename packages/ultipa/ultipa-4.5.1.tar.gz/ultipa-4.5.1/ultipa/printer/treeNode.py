# -*- coding: utf-8 -*-
# @Time    : 2023/7/19 12:06
# @Author  : Ultipa
# @Email   : support@ultipa.com
# @File    : treeNode.py
from ultipa.types.types import ExplainPlan


class TreeNode:

	def __init__(self, explain: ExplainPlan = None):
		self.explain = explain
		self.childNodes = []
