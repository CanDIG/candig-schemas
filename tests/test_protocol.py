"""
Tests for protocol.py
"""

import datetime
import unittest

import google.protobuf.message as message

import candig.schemas.protocol as protocol
import candig.schemas.candig.common_pb2 as common

from candig.schemas.candig.metadata_pb2 import Dataset


class TestProtocol(unittest.TestCase):
    """
    Test the methods in protocol.py
    """

    # TODO this suite is not very sophisticated right now due to
    # using empty instead of instantiated protobuf classes to test various
    # aspects of the protocol module...
    # an improvement would be to use an avrotools-like class instantiator
    # to generate dummy instantiations that could be tested

    def testGetValueListName(self):
        for clazz in protocol.getProtocolClasses():
            if len(clazz.DESCRIPTOR.fields_by_number) > 0:
                self.assertIsInstance(protocol.getValueListName(clazz), str)

    def testConvertDatetime(self):
        datetime_ = datetime.datetime.fromordinal(1234567)
        converted = protocol.convertDatetime(datetime_)
        self.assertEqual(converted, 44530905600000)

    def testGetValueFromValue(self):
        with self.assertRaises(TypeError):
            protocol.getValueFromValue(5)
        val = common.AttributeValue()
        with self.assertRaises(AttributeError):
            protocol.getValueFromValue(val)
        read = protocol.ReadAlignment()
        expected = "1"
        read.attributes.attr['key'].values.add().string_value = expected
        tag, value = list(read.attributes.attr.items())[0]
        result = protocol.getValueFromValue(value.values[0])
        self.assertEqual(result, expected)

    def testToJsonAndFromJson(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            jsonStr = protocol.toJson(obj)
            obj2 = protocol.fromJson(jsonStr, clazz)
            self.assertTrue(obj, obj2)

    def testToProtobufStringAndFromProtobufString(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            pbStr = protocol.toProtobufString(obj)
            obj2 = protocol.fromProtobufString(pbStr, clazz)
            self.assertTrue(obj, obj2)

    def testToJsonDict(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            jsonDict = protocol.toJsonDict(obj)
            self.assertIsInstance(jsonDict, dict)

    def testValidate(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            jsonStr = protocol.toJson(obj)
            protocol.validate(jsonStr, clazz)

    def testValidateProtobufString(self):
        classes = protocol.getProtocolClasses()
        for clazz in classes:
            obj = clazz()
            pbStr = protocol.toProtobufString(obj)
            protocol.validateProtobufString(pbStr, clazz)

    def testGetProtocolClasses(self):
        classes = protocol.getProtocolClasses()
        self.assertGreater(len(classes), 0)
        for clazz in classes:
            self.assertTrue(issubclass(clazz, message.Message))

    def testPostMethods(self):
        for postMethod in protocol.postMethods:
            self.assertEqual(len(postMethod), 3)
            self.assertIsInstance(postMethod[0], str)
            self.assertTrue(issubclass(postMethod[1], message.Message))
            self.assertTrue(issubclass(postMethod[2], message.Message))

    def testSetAttribute(self):
        expected = 5
        read = protocol.ReadAlignment()
        values = read.attributes.attr['key'].values
        protocol.setAttribute(values, expected)
        tag, value = list(read.attributes.attr.items())[0]
        result = value.values[0].int32_value
        self.assertEqual(result, expected)

    def testEncodeValue(self):
        expected = "5"
        result = protocol.encodeValue(expected)
        self.assertEqual(result[0].string_value, expected)
        listExpected = ["5", "6"]
        listResult = protocol.encodeValue(listExpected)
        self.assertEqual(listResult[0].string_value, listExpected[0])
        self.assertEqual(listResult[1].string_value, listExpected[1])

    def testDeepGetAttr(self):
        class Object(object):
            pass
        b = Object()
        setattr(b, "c", 42)
        a = Object()
        setattr(a, "b", b)
        obj = Object()
        setattr(obj, "a", a)
        setattr(obj, "d", 12)
        self.assertEqual(protocol.deepGetAttr(obj, "a.b.c"), 42)
        self.assertEqual(protocol.deepGetAttr(obj, "d"), 12)
        self.assertRaises(AttributeError,
                          protocol.deepGetAttr, obj, "a.b.x")
        self.assertRaises(AttributeError, protocol.deepGetAttr, obj, "e")

    def testDeepSetAttr(self):
        class Object(object):
            pass
        b = Object()
        setattr(b, "c", 42)
        a = Object()
        setattr(a, "b", b)
        obj = Object()
        setattr(obj, "a", a)
        protocol.deepSetAttr(obj, 'a.b.c', 43)
        self.assertEqual(obj.a.b.c, 43)
        protocol.deepSetAttr(obj, 'a.b.x', 12)
        self.assertEqual(obj.a.b.x, 12)
        self.assertRaises(AttributeError,
                          protocol.deepSetAttr, obj, "a.x.c", 42)


class TestRoundTrip(unittest.TestCase):
    """
    Instantiate the protocol classes and convert them to and from json
    and test if the values are preserved
    """
    def testRoundTripDatasetJson(self):
        id_ = "id"
        name = "name"
        description = "description"
        dataset = protocol.Dataset()
        dataset.id = id_
        dataset.name = name
        dataset.description = description
        jsonStr = protocol.toJson(dataset)
        newDataset = protocol.fromJson(jsonStr, Dataset)
        self.assertEqual(dataset.id, id_)
        self.assertEqual(dataset.name, name)
        self.assertEqual(dataset.description, description)
        datasetDict = protocol.toJsonDict(newDataset)
        self.assertEqual(datasetDict['id'], id_)
        self.assertEqual(datasetDict['name'], name)
        self.assertEqual(datasetDict['description'], description)

    def testRoundTripDatasetProtobufString(self):
        id_ = "id"
        name = "name"
        description = "description"
        dataset = protocol.Dataset()
        dataset.id = id_
        dataset.name = name
        dataset.description = description
        pbStr = protocol.toProtobufString(dataset)
        newDataset = protocol.fromProtobufString(pbStr, Dataset)
        self.assertEqual(newDataset.id, id_)
        self.assertEqual(newDataset.name, name)
        self.assertEqual(newDataset.description, description)
