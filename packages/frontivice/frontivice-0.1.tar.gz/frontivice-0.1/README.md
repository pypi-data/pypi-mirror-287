
# FRONTIVICE

  

This package is designed to generate regular expression formats based on device names. It simplifies the process of validating and parsing device identifiers by providing pre-defined regex patterns for various device types.

  

## Installation

  

You can install `frontivice` via pip. Use the following command:

  

```markdown

pip install frontivice

```

  

## Usage

  

Generate regular expression formats based on device names.

```markdown

from frontivice import Device

try:
    device = Device(device_name="OVF-AAAAAAATEY", device_type="olt")
    print(device.get_device_format())
except ValueError as e:
    print(e)


```

  
  

## Supported Device Names

- OLT

- OTB

- CA1

- CA2

- FTSBS

- CPE