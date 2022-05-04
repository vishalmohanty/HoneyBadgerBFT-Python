#
# Autogenerated by Thrift Compiler (0.16.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class VerificationKeyThrift(object):
    """
    Attributes:
     - key

    """


    def __init__(self, key=None,):
        self.key = key

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.key = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('VerificationKeyThrift')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 1)
            oprot.writeBinary(self.key)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.key is None:
            raise TProtocolException(message='Required field key is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PrivateKeyThrift(object):
    """
    Attributes:
     - key

    """


    def __init__(self, key=None,):
        self.key = key

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.key = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('PrivateKeyThrift')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 1)
            oprot.writeBinary(self.key)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.key is None:
            raise TProtocolException(message='Required field key is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EncryptedMessageThrift(object):
    """
    Attributes:
     - U
     - V
     - W

    """


    def __init__(self, U=None, V=None, W=None,):
        self.U = U
        self.V = V
        self.W = W

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.U = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.V = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.W = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('EncryptedMessageThrift')
        if self.U is not None:
            oprot.writeFieldBegin('U', TType.STRING, 1)
            oprot.writeBinary(self.U)
            oprot.writeFieldEnd()
        if self.V is not None:
            oprot.writeFieldBegin('V', TType.STRING, 2)
            oprot.writeBinary(self.V)
            oprot.writeFieldEnd()
        if self.W is not None:
            oprot.writeFieldBegin('W', TType.STRING, 3)
            oprot.writeBinary(self.W)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.U is None:
            raise TProtocolException(message='Required field U is unset!')
        if self.V is None:
            raise TProtocolException(message='Required field V is unset!')
        if self.W is None:
            raise TProtocolException(message='Required field W is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TPKEPublicKeyThrift(object):
    """
    Attributes:
     - l
     - k
     - VK
     - VKs

    """


    def __init__(self, l=None, k=None, VK=None, VKs=None,):
        self.l = l
        self.k = k
        self.VK = VK
        self.VKs = VKs

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.l = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.k = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.VK = VerificationKeyThrift()
                    self.VK.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.VKs = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = VerificationKeyThrift()
                        _elem5.read(iprot)
                        self.VKs.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TPKEPublicKeyThrift')
        if self.l is not None:
            oprot.writeFieldBegin('l', TType.I32, 1)
            oprot.writeI32(self.l)
            oprot.writeFieldEnd()
        if self.k is not None:
            oprot.writeFieldBegin('k', TType.I32, 2)
            oprot.writeI32(self.k)
            oprot.writeFieldEnd()
        if self.VK is not None:
            oprot.writeFieldBegin('VK', TType.STRUCT, 3)
            self.VK.write(oprot)
            oprot.writeFieldEnd()
        if self.VKs is not None:
            oprot.writeFieldBegin('VKs', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.VKs))
            for iter6 in self.VKs:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.l is None:
            raise TProtocolException(message='Required field l is unset!')
        if self.k is None:
            raise TProtocolException(message='Required field k is unset!')
        if self.VK is None:
            raise TProtocolException(message='Required field VK is unset!')
        if self.VKs is None:
            raise TProtocolException(message='Required field VKs is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TPKEPrivateKeyThrift(object):
    """
    Attributes:
     - PubKey
     - SK
     - i

    """


    def __init__(self, PubKey=None, SK=None, i=None,):
        self.PubKey = PubKey
        self.SK = SK
        self.i = i

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.PubKey = TPKEPublicKeyThrift()
                    self.PubKey.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.SK = PrivateKeyThrift()
                    self.SK.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.i = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TPKEPrivateKeyThrift')
        if self.PubKey is not None:
            oprot.writeFieldBegin('PubKey', TType.STRUCT, 1)
            self.PubKey.write(oprot)
            oprot.writeFieldEnd()
        if self.SK is not None:
            oprot.writeFieldBegin('SK', TType.STRUCT, 2)
            self.SK.write(oprot)
            oprot.writeFieldEnd()
        if self.i is not None:
            oprot.writeFieldBegin('i', TType.I32, 3)
            oprot.writeI32(self.i)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.PubKey is None:
            raise TProtocolException(message='Required field PubKey is unset!')
        if self.SK is None:
            raise TProtocolException(message='Required field SK is unset!')
        if self.i is None:
            raise TProtocolException(message='Required field i is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DealerThrift(object):
    """
    Attributes:
     - PubKey
     - PrivKeys

    """


    def __init__(self, PubKey=None, PrivKeys=None,):
        self.PubKey = PubKey
        self.PrivKeys = PrivKeys

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.PubKey = TPKEPublicKeyThrift()
                    self.PubKey.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.PrivKeys = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = TPKEPrivateKeyThrift()
                        _elem12.read(iprot)
                        self.PrivKeys.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DealerThrift')
        if self.PubKey is not None:
            oprot.writeFieldBegin('PubKey', TType.STRUCT, 1)
            self.PubKey.write(oprot)
            oprot.writeFieldEnd()
        if self.PrivKeys is not None:
            oprot.writeFieldBegin('PrivKeys', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.PrivKeys))
            for iter13 in self.PrivKeys:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.PubKey is None:
            raise TProtocolException(message='Required field PubKey is unset!')
        if self.PrivKeys is None:
            raise TProtocolException(message='Required field PrivKeys is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AESKey(object):
    """
    Attributes:
     - key

    """


    def __init__(self, key=None,):
        self.key = key

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.key = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AESKey')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 1)
            oprot.writeBinary(self.key)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.key is None:
            raise TProtocolException(message='Required field key is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(VerificationKeyThrift)
VerificationKeyThrift.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'key', 'BINARY', None, ),  # 1
)
all_structs.append(PrivateKeyThrift)
PrivateKeyThrift.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'key', 'BINARY', None, ),  # 1
)
all_structs.append(EncryptedMessageThrift)
EncryptedMessageThrift.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'U', 'BINARY', None, ),  # 1
    (2, TType.STRING, 'V', 'BINARY', None, ),  # 2
    (3, TType.STRING, 'W', 'BINARY', None, ),  # 3
)
all_structs.append(TPKEPublicKeyThrift)
TPKEPublicKeyThrift.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'l', None, None, ),  # 1
    (2, TType.I32, 'k', None, None, ),  # 2
    (3, TType.STRUCT, 'VK', [VerificationKeyThrift, None], None, ),  # 3
    (4, TType.LIST, 'VKs', (TType.STRUCT, [VerificationKeyThrift, None], False), None, ),  # 4
)
all_structs.append(TPKEPrivateKeyThrift)
TPKEPrivateKeyThrift.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'PubKey', [TPKEPublicKeyThrift, None], None, ),  # 1
    (2, TType.STRUCT, 'SK', [PrivateKeyThrift, None], None, ),  # 2
    (3, TType.I32, 'i', None, None, ),  # 3
)
all_structs.append(DealerThrift)
DealerThrift.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'PubKey', [TPKEPublicKeyThrift, None], None, ),  # 1
    (2, TType.LIST, 'PrivKeys', (TType.STRUCT, [TPKEPrivateKeyThrift, None], False), None, ),  # 2
)
all_structs.append(AESKey)
AESKey.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'key', 'BINARY', None, ),  # 1
)
fix_spec(all_structs)
del all_structs
