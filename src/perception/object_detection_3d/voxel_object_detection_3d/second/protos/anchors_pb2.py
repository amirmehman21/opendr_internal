# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: second/protos/anchors.proto

import sys
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="second/protos/anchors.proto",
    package="second.protos",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1bsecond/protos/anchors.proto\x12\rsecond.protos"\xa2\x01\n\x12\x41nchorGeneratorOld\x12\x12\n\nclas' +
        's_name\x18\x01 \x01(\t\x12\x11\n\tbev_range\x18\x02 \x03(\x02\x12\x17\n\x0f\x61nchor_center' +
        '_z\x18\x03 \x01(\x02\x12\x14\n\x0c\x61nchor_sizes\x18\x04 \x03(\x02\x12\x19\n\x11matched_thresh' +
        'old\x18\x05 \x01(\x02\x12\x1b\n\x13unmatched_threshold\x18\x06 \x01(\x02"\xa7\x01\n\x15\x41nchor' +
        'GeneratorStride\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\r\n\x05siz' +
        'es\x18\x02 \x03(\x02\x12\x0f\n\x07strides\x18\x03 \x03(\x02\x12\x0f\n\x07offse' +
        'ts\x18\x04 \x03(\x02\x12\x11\n\trotations\x18\x05 \x03(\x02\x12\x19\n\x11matched' +
        '_threshold\x18\x06 \x01(\x02\x12\x1b\n\x13unmatched_threshold\x18\x07 \x01(\x02"\x9b\x01\n\x14\x41ncho' +
        'rGeneratorRange\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\r\n\x05siz' +
        'es\x18\x02 \x03(\x02\x12\x15\n\ranchor_ranges\x18\x03 \x03(\x02\x12\x11\n\tr' +
        'otations\x18\x04 \x03(\x02\x12\x19\n\x11matched_threshold\x18\x05 \x01(\x02\x12\x1b\n\x13unmatch' +
        'ed_threshold\x18\x06 \x01(\x02"\x82\x02\n\x19\x41nchorGeneratorCollection\x12G\n\x17\x61nchor_' +
        'generator_stride\x18\x01 \x01(\x0b\x32$.second.protos.AnchorGeneratorSt' +
        'rideH\x00\x12\x45\n\x16\x61nchor_generator_range\x18\x02 \x01(\x0b\x32#.second.pr' +
        'otos.AnchorGeneratorRangeH\x00\x12\x41\n\x14\x61nchor_generator_' +
        'old\x18\x03 \x01(\x0b\x32!.second.protos.AnchorGeneratorOldH\x00\x42\x12\n\x10\x61nchor' +
        '_generator"\xa8\x01\n\x16\x41nchorGenerator_depara\x12\x12\n\nclass_' +
        'name\x18\x01 \x01(\t\x12\r\n\x05sizes\x18\x02 \x03(\x02\x12\x0f\n\x07stride' +
        's\x18\x03 \x03(\x02\x12\x0f\n\x07offsets\x18\x04 \x03(\x02\x12\x11\n\trot' +
        'ations\x18\x05 \x03(\x02\x12\x19\n\x11matched_threshold\x18\x06 \x01(\x02\x12\x1b\n\x13un' +
        'matched_threshold\x18\x07 \x01(\x02"z\n\x11\x41nchorGeneratorV1\x12\x17\n\x0f\x61nchor_' +
        'center_z\x18\x01 \x01(\x02\x12\x14\n\x0c\x61nchor_sizes\x18\x02 \x03(\x02\x12\x19\n\x11matc' +
        'hed_threshold\x18\x03 \x01(\x02\x12\x1b\n\x13unmatched_threshold\x18\x04 \x01(\x02\x62\x06proto3'
    ),
)


_ANCHORGENERATOROLD = _descriptor.Descriptor(
    name="AnchorGeneratorOld",
    full_name="second.protos.AnchorGeneratorOld",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="class_name",
            full_name="second.protos.AnchorGeneratorOld.class_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bev_range",
            full_name="second.protos.AnchorGeneratorOld.bev_range",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="anchor_center_z",
            full_name="second.protos.AnchorGeneratorOld.anchor_center_z",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="anchor_sizes",
            full_name="second.protos.AnchorGeneratorOld.anchor_sizes",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="matched_threshold",
            full_name="second.protos.AnchorGeneratorOld.matched_threshold",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="unmatched_threshold",
            full_name="second.protos.AnchorGeneratorOld.unmatched_threshold",
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=47,
    serialized_end=209,
)


_ANCHORGENERATORSTRIDE = _descriptor.Descriptor(
    name="AnchorGeneratorStride",
    full_name="second.protos.AnchorGeneratorStride",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="class_name",
            full_name="second.protos.AnchorGeneratorStride.class_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sizes",
            full_name="second.protos.AnchorGeneratorStride.sizes",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="strides",
            full_name="second.protos.AnchorGeneratorStride.strides",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="offsets",
            full_name="second.protos.AnchorGeneratorStride.offsets",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rotations",
            full_name="second.protos.AnchorGeneratorStride.rotations",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="matched_threshold",
            full_name="second.protos.AnchorGeneratorStride.matched_threshold",
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="unmatched_threshold",
            full_name="second.protos.AnchorGeneratorStride.unmatched_threshold",
            index=6,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=212,
    serialized_end=379,
)


_ANCHORGENERATORRANGE = _descriptor.Descriptor(
    name="AnchorGeneratorRange",
    full_name="second.protos.AnchorGeneratorRange",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="class_name",
            full_name="second.protos.AnchorGeneratorRange.class_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sizes",
            full_name="second.protos.AnchorGeneratorRange.sizes",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="anchor_ranges",
            full_name="second.protos.AnchorGeneratorRange.anchor_ranges",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rotations",
            full_name="second.protos.AnchorGeneratorRange.rotations",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="matched_threshold",
            full_name="second.protos.AnchorGeneratorRange.matched_threshold",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="unmatched_threshold",
            full_name="second.protos.AnchorGeneratorRange.unmatched_threshold",
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=382,
    serialized_end=537,
)


_ANCHORGENERATORCOLLECTION = _descriptor.Descriptor(
    name="AnchorGeneratorCollection",
    full_name="second.protos.AnchorGeneratorCollection",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="anchor_generator_stride",
            full_name="second.protos.AnchorGeneratorCollection.anchor_generator_stride",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="anchor_generator_range",
            full_name="second.protos.AnchorGeneratorCollection.anchor_generator_range",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="anchor_generator_old",
            full_name="second.protos.AnchorGeneratorCollection.anchor_generator_old",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="anchor_generator",
            full_name="second.protos.AnchorGeneratorCollection.anchor_generator",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=540,
    serialized_end=798,
)


_ANCHORGENERATOR_DEPARA = _descriptor.Descriptor(
    name="AnchorGenerator_depara",
    full_name="second.protos.AnchorGenerator_depara",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="class_name",
            full_name="second.protos.AnchorGenerator_depara.class_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sizes",
            full_name="second.protos.AnchorGenerator_depara.sizes",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="strides",
            full_name="second.protos.AnchorGenerator_depara.strides",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="offsets",
            full_name="second.protos.AnchorGenerator_depara.offsets",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="rotations",
            full_name="second.protos.AnchorGenerator_depara.rotations",
            index=4,
            number=5,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="matched_threshold",
            full_name="second.protos.AnchorGenerator_depara.matched_threshold",
            index=5,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="unmatched_threshold",
            full_name="second.protos.AnchorGenerator_depara.unmatched_threshold",
            index=6,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=801,
    serialized_end=969,
)


_ANCHORGENERATORV1 = _descriptor.Descriptor(
    name="AnchorGeneratorV1",
    full_name="second.protos.AnchorGeneratorV1",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="anchor_center_z",
            full_name="second.protos.AnchorGeneratorV1.anchor_center_z",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="anchor_sizes",
            full_name="second.protos.AnchorGeneratorV1.anchor_sizes",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="matched_threshold",
            full_name="second.protos.AnchorGeneratorV1.matched_threshold",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="unmatched_threshold",
            full_name="second.protos.AnchorGeneratorV1.unmatched_threshold",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=971,
    serialized_end=1093,
)

_ANCHORGENERATORCOLLECTION.fields_by_name[
    "anchor_generator_stride"
].message_type = _ANCHORGENERATORSTRIDE
_ANCHORGENERATORCOLLECTION.fields_by_name[
    "anchor_generator_range"
].message_type = _ANCHORGENERATORRANGE
_ANCHORGENERATORCOLLECTION.fields_by_name[
    "anchor_generator_old"
].message_type = _ANCHORGENERATOROLD
_ANCHORGENERATORCOLLECTION.oneofs_by_name["anchor_generator"].fields.append(
    _ANCHORGENERATORCOLLECTION.fields_by_name["anchor_generator_stride"]
)
_ANCHORGENERATORCOLLECTION.fields_by_name[
    "anchor_generator_stride"
].containing_oneof = _ANCHORGENERATORCOLLECTION.oneofs_by_name["anchor_generator"]
_ANCHORGENERATORCOLLECTION.oneofs_by_name["anchor_generator"].fields.append(
    _ANCHORGENERATORCOLLECTION.fields_by_name["anchor_generator_range"]
)
_ANCHORGENERATORCOLLECTION.fields_by_name[
    "anchor_generator_range"
].containing_oneof = _ANCHORGENERATORCOLLECTION.oneofs_by_name["anchor_generator"]
_ANCHORGENERATORCOLLECTION.oneofs_by_name["anchor_generator"].fields.append(
    _ANCHORGENERATORCOLLECTION.fields_by_name["anchor_generator_old"]
)
_ANCHORGENERATORCOLLECTION.fields_by_name[
    "anchor_generator_old"
].containing_oneof = _ANCHORGENERATORCOLLECTION.oneofs_by_name["anchor_generator"]
DESCRIPTOR.message_types_by_name["AnchorGeneratorOld"] = _ANCHORGENERATOROLD
DESCRIPTOR.message_types_by_name["AnchorGeneratorStride"] = _ANCHORGENERATORSTRIDE
DESCRIPTOR.message_types_by_name["AnchorGeneratorRange"] = _ANCHORGENERATORRANGE
DESCRIPTOR.message_types_by_name[
    "AnchorGeneratorCollection"
] = _ANCHORGENERATORCOLLECTION
DESCRIPTOR.message_types_by_name["AnchorGenerator_depara"] = _ANCHORGENERATOR_DEPARA
DESCRIPTOR.message_types_by_name["AnchorGeneratorV1"] = _ANCHORGENERATORV1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnchorGeneratorOld = _reflection.GeneratedProtocolMessageType(
    "AnchorGeneratorOld",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANCHORGENERATOROLD,
        __module__="second.protos.anchors_pb2"
        # @@protoc_insertion_point(class_scope:second.protos.AnchorGeneratorOld)
    ),
)
_sym_db.RegisterMessage(AnchorGeneratorOld)

AnchorGeneratorStride = _reflection.GeneratedProtocolMessageType(
    "AnchorGeneratorStride",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANCHORGENERATORSTRIDE,
        __module__="second.protos.anchors_pb2"
        # @@protoc_insertion_point(class_scope:second.protos.AnchorGeneratorStride)
    ),
)
_sym_db.RegisterMessage(AnchorGeneratorStride)

AnchorGeneratorRange = _reflection.GeneratedProtocolMessageType(
    "AnchorGeneratorRange",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANCHORGENERATORRANGE,
        __module__="second.protos.anchors_pb2"
        # @@protoc_insertion_point(class_scope:second.protos.AnchorGeneratorRange)
    ),
)
_sym_db.RegisterMessage(AnchorGeneratorRange)

AnchorGeneratorCollection = _reflection.GeneratedProtocolMessageType(
    "AnchorGeneratorCollection",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANCHORGENERATORCOLLECTION,
        __module__="second.protos.anchors_pb2"
        # @@protoc_insertion_point(class_scope:second.protos.AnchorGeneratorCollection)
    ),
)
_sym_db.RegisterMessage(AnchorGeneratorCollection)

AnchorGenerator_depara = _reflection.GeneratedProtocolMessageType(
    "AnchorGenerator_depara",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANCHORGENERATOR_DEPARA,
        __module__="second.protos.anchors_pb2"
        # @@protoc_insertion_point(class_scope:second.protos.AnchorGenerator_depara)
    ),
)
_sym_db.RegisterMessage(AnchorGenerator_depara)

AnchorGeneratorV1 = _reflection.GeneratedProtocolMessageType(
    "AnchorGeneratorV1",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ANCHORGENERATORV1,
        __module__="second.protos.anchors_pb2"
        # @@protoc_insertion_point(class_scope:second.protos.AnchorGeneratorV1)
    ),
)
_sym_db.RegisterMessage(AnchorGeneratorV1)


# @@protoc_insertion_point(module_scope)
