
import sys
import json
import os
import re
import argparse

def cleanup_doc(doc,indent=0):
  return '\n'.join([' '*indent + line for line in doc.split('\n')])

def get_file_locations():
  parser = argparse.ArgumentParser()
  parser.add_argument('input', help='Input Protobuf JSON filename(s)', nargs='+')
  parser.add_argument('output', help='Output directory')
  args = parser.parse_args()
  return (args.input, args.output)

def typename(typeobject):
  if isinstance(typeobject, list):
    union_names = [typename(item) for item in typeobject]
    return '|'.join(union_names)

  elif isinstance(typeobject, dict):
    if typeobject['type'] == 'array':
      return 'array<%s>' % typename(typeobject['items'])
    elif typeobject['type'] == 'map':
      return 'map<%s, %s>' % (typename(typeobject['key']), typename(typeobject['value']))
    else:
      raise Exception("Unsupported type object: %s" %(typeobject['type']))

  elif isinstance(typeobject, str):
    return typeobject

  raise ValueError

if __name__ == '__main__':

  json_filenames, rest_directory = get_file_locations()

  for json_filename in json_filenames:
    base_filename = os.path.basename(json_filename)
    name = os.path.splitext(base_filename)[0]

    rest_filename = os.path.join(rest_directory, name+'.rst')

    with open(json_filename,'r') as f:
      data = json.load(f)

    output = data['protocol'] + '\n'
    output += '*' * len(data['protocol']) + '\n\n'

    if 'doc' in data:
      output += cleanup_doc(data['doc']) + '\n\n'

    for message_name in data['messages']:
      message_def = data['messages'][message_name]
      doc = message_def['doc']
      # process formal parameters ('request')
      request = message_def['request']
      # collect the names
      param_names = []
      for param in request:
        param_names.append(param['name'])
      response = message_def['response']
      errors = message_def['errors']
      output += " .. function:: %s(%s)\n\n" % (message_name,
                                               ', '.join(param_names))
      for param in request:
        output += "  :param %s: %s\n" % (param['name'], param['type'])
      output += "  :return type: %s\n" % response
      output += "  :throws: %s\n\n" % ', '.join(errors)
      output += cleanup_doc(doc)
      output += "\n\n"

    for item in data['types']:
      output += '.. protobuf:%s:: %s\n\n' % (item['type'], item['name'])

      if item['type'] == 'message':
        for field in item['fields']:
          output += '  :field %s:\n' % field['name']
          if 'doc' in field:
            output += cleanup_doc(field['doc'],indent=4) + '\n'
          output += '  :type %s: %s\n' % (field['name'], typename(field['type']))
        output += '\n'

      if item['type'] == 'enum':
        output += '  :symbols: %s\n' % '|'.join(item['symbols'])

      if item['type'] == 'fixed':
        output += '  :size: %s\n' % item['size']

      if 'doc' in item:
        output += cleanup_doc(item['doc'],indent=2) + '\n\n'

    with open(rest_filename,'w') as f:
      f.write(output)
