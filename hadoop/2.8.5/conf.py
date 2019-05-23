#!/usr/bin/python3

import os
import sys
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM


def parse(root: ET.Element) -> dict:
    return {
        conf.find('name').text: conf.find('value').text
        for conf in root.iter('property')
    }


def load(filepath: str) -> dict:
    if not os.path.exists(filepath):
        return {}

    root = ET.parse(filepath).getroot()
    return parse(root)


def load_string(content: str) -> dict:
    root = ET.fromstring(content)
    return parse(root)


def write(filepath: str, properties: dict) -> None:
    root = ET.Element('configuration')

    for name, value in properties.items():
        if value:
            conf = ET.SubElement(root, 'property')
            ET.SubElement(conf, 'name').text = name
            ET.SubElement(conf, 'value').text = value
        else:
            print('{:s} is reset to default'.format(name))

    content = ET.tostring(root, encoding='UTF-8')
    pretty = DOM.parseString(content).toprettyxml(encoding='UTF-8')

    with open(filepath, 'bw') as f:
        f.write(pretty)


def main(filepath):
    properties = load(filepath)
    overrided = load_string('\n'.join(sys.stdin.readlines()))

    properties.update(overrided)
    write(filepath, properties)


def error(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(-1)


if __name__ == "__main__":
    conf_dir = os.environ.get('HADOOP_CONF_DIR')
    if not conf_dir:
        conf_dir = os.environ.get('HADOOP_HOME')
        if conf_dir:
            conf_dir = os.path.join(conf_dir, 'etc/hadoop')
        else:
            error("HADOOP_CONF_DIR or HADOOP_HOME not set")

    if len(sys.argv) < 2:
        error("One of args in ['core', 'hdfs', 'mapred', 'yarn'] required")

    which = sys.argv[1]
    if which not in ['core', 'hdfs', 'mapred', 'yarn']:
        error("Only ['core', 'hdfs', 'mapred', 'yarn'] supported")

    filepath = os.path.join(conf_dir, '{:s}-site.xml'.format(which))
    main(filepath)

    print('File {:s} updated'.format(filepath))
