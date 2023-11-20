# Xiaomi Community AutoTask

A Python script for automatically completing Xiaomi community points tasks

Modified to compatible with [miui-auto-tasks](https://github.com/0-8-4/miui-auto-tasks)' v1.6.0 config file

# Support environment

The script only support **Python3.9**

# How to use

1. Configure as what you needs in `config.yaml`. 
   For details, refer to [here](https://github.com/0-8-4/miui-auto-tasks/wiki#配置文件). Configurations about UA and ONEPUSH take no effects.

2. Make sure you have installed the execjs, requests and cv2 module, or install them manually

   ```bash
   pip install -r requirements.txt
   ```

3. Run `xiaomi.py` and enjoy

# Change Log

## 2023-11-19

- Added compatibility with [miui-auto-tasks](https://github.com/0-8-4/miui-auto-tasks)' v1.6.0 config file

## 2023-11-18

- Fix token acquisition
- Package the functions into a binary file

## 2023-11-12

- Token acquisition support
- Multi-account support

## 2023-11-11

- Fixed `check_in` by adding token validation

## 2023-11-09

- First build
