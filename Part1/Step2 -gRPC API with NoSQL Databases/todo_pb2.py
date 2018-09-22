# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='myTodos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntodo.proto\x12\x07myTodos\"D\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x64one\x18\x04 \x01(\x08\"\'\n\x08TodoList\x12\x1b\n\x04todo\x18\x01 \x03(\x0b\x32\r.myTodos.Todo\"\x14\n\x06TodoId\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xe1\x01\n\x0cTodosService\x12)\n\x04List\x12\x0e.myTodos.Empty\x1a\x11.myTodos.TodoList\x12\'\n\x06Insert\x12\r.myTodos.Todo\x1a\x0e.myTodos.Empty\x12)\n\x03Get\x12\x0f.myTodos.TodoId\x1a\x11.myTodos.TodoList\x12)\n\x06Remove\x12\x0f.myTodos.TodoId\x1a\x0e.myTodos.Empty\x12\'\n\x06Update\x12\r.myTodos.Todo\x1a\x0e.myTodos.Emptyb\x06proto3')
)




_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='myTodos.Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='myTodos.Todo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='myTodos.Todo.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='myTodos.Todo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='myTodos.Todo.done', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=91,
)


_TODOLIST = _descriptor.Descriptor(
  name='TodoList',
  full_name='myTodos.TodoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todo', full_name='myTodos.TodoList.todo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=132,
)


_TODOID = _descriptor.Descriptor(
  name='TodoId',
  full_name='myTodos.TodoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='myTodos.TodoId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=154,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='myTodos.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=163,
)

_TODOLIST.fields_by_name['todo'].message_type = _TODO
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['TodoList'] = _TODOLIST
DESCRIPTOR.message_types_by_name['TodoId'] = _TODOID
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:myTodos.Todo)
  ))
_sym_db.RegisterMessage(Todo)

TodoList = _reflection.GeneratedProtocolMessageType('TodoList', (_message.Message,), dict(
  DESCRIPTOR = _TODOLIST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:myTodos.TodoList)
  ))
_sym_db.RegisterMessage(TodoList)

TodoId = _reflection.GeneratedProtocolMessageType('TodoId', (_message.Message,), dict(
  DESCRIPTOR = _TODOID,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:myTodos.TodoId)
  ))
_sym_db.RegisterMessage(TodoId)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:myTodos.Empty)
  ))
_sym_db.RegisterMessage(Empty)



_TODOSSERVICE = _descriptor.ServiceDescriptor(
  name='TodosService',
  full_name='myTodos.TodosService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=166,
  serialized_end=391,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='myTodos.TodosService.List',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_TODOLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='myTodos.TodosService.Insert',
    index=1,
    containing_service=None,
    input_type=_TODO,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='myTodos.TodosService.Get',
    index=2,
    containing_service=None,
    input_type=_TODOID,
    output_type=_TODOLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='myTodos.TodosService.Remove',
    index=3,
    containing_service=None,
    input_type=_TODOID,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='myTodos.TodosService.Update',
    index=4,
    containing_service=None,
    input_type=_TODO,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSSERVICE)

DESCRIPTOR.services_by_name['TodosService'] = _TODOSSERVICE

# @@protoc_insertion_point(module_scope)
