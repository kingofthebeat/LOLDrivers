import sys
import argparse
import os
import csv
import yaml


def writeYmlFile(file_path : str, obj : dict) -> None:
    with open(file_path, 'w') as outfile:
        yaml.dump(obj, outfile, default_flow_style=False, sort_keys=False)


def generate_yml_files(csv_file_path, output_folder):
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count = line_count + 1
                continue
            line_count = line_count + 1
            yaml_data = dict()
            yaml_data["Name"] = row[0]
            yaml_data["Author"] = row[1]
            yaml_data["Created"] = row[2]
            yaml_data["MitreID"] = row[9]
            yaml_data["Category"] = row[7]
            yaml_data["Verified"] = row[30]
            commands_data = dict()
            commands_data["Command"] = row[4]
            if commands_data["Command"] == '':
                sc_example = "sc.exe create " + yaml_data['Name'] + " binPath=C:\\windows\\temp\\" + yaml_data['Name'] + " type=kernel" \
                    + "\nsc.exe start " + yaml_data['Name']
                commands_data["Command"] = sc_example
            commands_data["Description"] = row[5]
            commands_data["Usecase"] = row[6]
            commands_data["Privileges"] = row[8]
            commands_data["OperatingSystem"] = row[10]
            yaml_data["Commands"] = commands_data
            resources_data = list()
            for Resource in row[11].split(", "):
                if Resource.startswith("Link:"):
                    resources_data.append(Resource[5:])
            yaml_data["Resources"] = resources_data
            yaml_data["driver_description"] = row[12]
            acknowledgement_data = dict()
            acknowledgement_data["Person"] = row[14]
            acknowledgement_data["Handle"] = row[15]
            yaml_data["Acknowledgement"] = acknowledgement_data
            detection_data = list()
            for detection in row[16].split(", "):
                if detection.startswith("IOC"):
                    detection_data.append({
                        "type": 'IOC',
                        "value": detection[5:]
                    })
                elif detection.startswith("BlockRule"):
                    detection_data.append({
                        "type": 'BlockRule',
                        "value": detection[11:]
                    })    
            yaml_data["Detection"] = detection_data
            KnownHashes_data = list()
            for KnownHashes in row[17].split(", "):
                if KnownHashes.startswith("hash:"):
                    hash = dict()
                    hash['Filename'] = row[0]
                    
                    hash_ = KnownHashes[5:].lstrip().strip()
                    if len(hash) == 32:
                        hash['MD5'] = hash_
                    else:
                        hash['MD5'] = ''
                    if len(hash) == 40:
                        hash['SHA1'] = hash_
                    else:
                        hash['SHA1'] = ''
                    if len(hash) == 64:
                        hash['SHA256'] = hash_
                    else:
                        hash['SHA256'] = ''
                    
                    hash["Signature"] = row[20]
                    hash["Date"] = row[21]
                    hash["Publisher"] = row[22]
                    hash["Company"] = row[23]
                    hash["Description"] = row[24]
                    hash["Product"] = row[25]
                    hash["ProductVersion"] = row[26]
                    hash["FileVersion"] = row[27]
                    hash["MachineType"] = row[28]
                    hash["OriginalFilename"] = row[29]
                    KnownHashes_data.append(hash)
            yaml_data["KnownVulnerableSamples"] = KnownHashes_data

            file_name = os.path.splitext(yaml_data["Name"])[0] + '.yaml'
            writeYmlFile(os.path.join('yaml/' + output_folder, file_name), yaml_data)               


def generate(args):
    generate_yml_files(args.input, args.output)


def main(args):
    parser = argparse.ArgumentParser(
    description="loldriver yaml file generator")
    parser.add_argument("-i", "--input", required=False, default="drivers.csv",
            help="input csv file containing drivers.csv data, defaults to: drivers.csv")
    parser.add_argument("-o", "--output", required=False, default=".",
                        help="output folder, defaults to '.'")

    parser.set_defaults(func=generate)

    args = parser.parse_args()
    
    return args.func(args)

if __name__ == "__main__":
    main(sys.argv[1:])
