# -*- coding: utf-8 -*-
#  Copyright (C) 2021- BOUFFALO LAB (NANJING) CO., LTD.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import re
import os
import sys
import time
import shutil
import hashlib
import lzma

try:
    import bflb_path
except ImportError:
    from libs import bflb_path
from libs import bflb_utils
from libs import bflb_pt_creater as partition
from libs import bflb_ro_params_device_tree as bl_ro_device_tree
from libs import bflb_fw_check_partition as pt_check
from libs.bflb_utils import img_create_encrypt_data
from libs.bflb_utils import img_create_encrypt_data_xts


version_str = "V1.2.3"

chip_dict = (
    "bl602",
    "bl604",
    "bl702",
    "bl704",
    "bl706",
    "bl702l",
    "bl704l",
    "bl606p",
    "bl808",
    "bl616",
    "bl618",
    "bl628",
)


def dump_release_note():
    vxxx_rn = ""
    ################################
    vxxx_rn += """
    ---V1.2.3---
    Feature:
        1. support crc check for encrypted efusedata.bin
    """
    ################################
    vxxx_rn += """
    ---V1.2.2.1---
    Feature:
        1. temp version for RD
    """
    ################################
    vxxx_rn += """
    ---V1.2.2---
    Feature:
        1. support ram image
        2. support --exxx like efuse option
    """
    ################################
    vxxx_rn += """
    ---V1.2.1---
    Feature:
        1. support checkpartition option
    """
    ################################
    bflb_utils.printf()
    vxxx_rn += """
    ---V1.2.0---
    Feature:
        1. support all chip image create with bootheader update
        2. support all chip encrypt and sign
    """
    bflb_utils.printf(vxxx_rn)


def get_nicky_name(chipname):
    if chipname == "bl604":
        return "bl602"
    if chipname == "bl704" or chipname == "bl706":
        return "bl702"
    if chipname == "bl704l":
        return "bl702l"
    if chipname == "bl618":
        return "bl616"
    return chipname


def parse_header(bin):
    try:
        with open(bin, "rb") as fp:
            content = fp.read()
            if content[0:4] == b"BFNP" or content[0:4] == b"BFAP":
                return True
    except Exception as e:
        bflb_utils.printf(e)
        bflb_utils.printf("[Warning] Check header fail")
    return False


def get_value_file(path, chipname, cpu_id=None):
    if cpu_id:
        path = path.replace("$(CHIPNAME)", chipname + "_" + cpu_id)
    else:
        path = path.replace("$(CHIPNAME)", chipname)
    if os.path.isabs(path):
        path = os.path.abspath(path)

    # judge file path
    if not os.path.exists(path):
        dir_path = os.path.dirname(path)
        file_name = os.path.basename(path)
        try:
            all_file_list = os.listdir(dir_path)
        except Exception as e:
            bflb_utils.printf(e)
            return None
        result = []
        if "*" in file_name:
            file_name = file_name.replace(".", "\\.").replace("*", ".*[\u4e00-\u9fa5]*")
        for one_name in all_file_list:
            pattern = re.compile("^" + file_name + "$")
            result += pattern.findall(one_name)
        if len(result) > 1:
            bflb_utils.printf("[Error] Multiple files were matched! ")
            return None
        if len(result) == 0:
            error = "[Error]: " + path + " image file is not existed"
            bflb_utils.printf(error)
            return None
        else:
            path = os.path.join(dir_path, result[0])

    return path


def get_img_file_list(files, chipname, cpu_id):
    file_list = files.split(",")
    final = []
    for file in file_list:
        ret = get_value_file(file, chipname, cpu_id)
        if ret != None:
            final.append(ret)
        else:
            bflb_utils.printf("[Error] Get ", file, " Fail!!!!")
    return final


def parse_rfpa(bin, dts_bytearray):
    try:
        length = len(dts_bytearray)
        with open(bin, "rb") as fp:
            content = fp.read()
            bin_bytearray = bytearray(content)
            if (
                content[0:4] == b"BFNP"
                and (
                    content[0 + 4096 : 4 + 4096] == b"BFAP"
                    or content[0 + 4096 : 4 + 4096] == b"BFNP"
                )
                and content[1024 + 8192 : 1032 + 8192] == b"BLRFPARA"
            ):
                bflb_utils.printf("8K header found,append dts file for")
                bin_bytearray[1032 + 8192 : 1032 + 8192 + length] = dts_bytearray
                with open(bin, "wb") as fp:
                    fp.write(bin_bytearray)
                return
            if content[0:4] == b"BFNP" and content[1024 + 4096 : 1032 + 4096] == b"BLRFPARA":
                bflb_utils.printf("4K header found,append dts file")
                bin_bytearray[1032 + 4096 : 1032 + 4096 + length] = dts_bytearray
                with open(bin, "wb") as fp:
                    fp.write(bin_bytearray)
                return
            if content[1024:1032] == b"BLRFPARA":
                bflb_utils.printf("Raw image found,append dts file")
                bin_bytearray[1032 : 1032 + length] = dts_bytearray
                with open(bin, "wb") as fp:
                    fp.write(bin_bytearray)
                return
            bflb_utils.printf("BLRFPARA magic not found, skip append dts file")
    except Exception as e:
        bflb_utils.printf(e)
        bflb_utils.printf("[Error] Append dts file fail")


def found_file(dir, suffix):
    files = []
    dir = dir.replace("'", "").replace('"', "")
    # return all files as a list
    for file in os.listdir(dir):
        # check the files which are end with specific extension
        if file.endswith(suffix):
            # print path name of selected files
            files.append(file)
    return files


def found_boot2_mfg_file(dir, target):
    files = []
    dir = dir.replace("'", "").replace('"', "")
    # return all files as a list
    for file in os.listdir(dir):
        # check the files which are end with specific extension
        if file.startswith(target) and file.endswith(".bin"):
            # print path name of selected files
            files.append(file)
    return files


def create_partiton_table(search_dir, imgfile):
    # search_dir=args.brdcfgdir
    files = found_file(search_dir, ".toml")
    if len(files) == 0:
        bflb_utils.printf("[Warning] No partiton file found in ", search_dir, ",go on next steps")
        return
    if len(files) > 1:
        bflb_utils.printf(
            "[Error] More than one partition file found in ", search_dir, ",go on next steps"
        )
        return
    bflb_utils.printf("Create partition using ", files[0])
    pt_helper = partition.PtCreater(os.path.join(search_dir, files[0]))
    filedir, ext = os.path.split(imgfile)
    pt_helper.create_pt_table(os.path.join(filedir, "partition.bin"))


def append_dts_file(search_dir, imgfile):
    # search_dir=args.brdcfgdir
    files = found_file(search_dir, ".dts")
    if len(files) == 0:
        bflb_utils.printf("[Warning] No dts file found in ", search_dir, ",go on next steps")
        return
    if len(files) > 1:
        bflb_utils.printf(
            "[Error] More than one dts file found in ", search_dir, ",go on next steps"
        )
        return
    bflb_utils.printf("Create dts for ", imgfile)
    bflb_utils.printf("Create dts using ", files[0])
    try:
        dts_hex = bl_ro_device_tree.bl_dts2hex(os.path.join(search_dir, files[0]))
        dts_bytearray = bflb_utils.hexstr_to_bytearray(dts_hex)
    except Exception as e:
        bflb_utils.printf(e)
        bflb_utils.printf("[Error] Create fail!!!, go on next steps")
        return
    parse_rfpa(imgfile, dts_bytearray)


def copy_boot2_file(search_dir, imgfile):
    # search_dir=args.brdcfgdir
    files = found_boot2_mfg_file(search_dir, "boot")
    if len(files) == 0:
        bflb_utils.printf(
            "[Warning] No boot2/bootloader file found in ", search_dir, ",go on next steps"
        )
        return
    if len(files) > 1:
        bflb_utils.printf(
            "[Error] More than one boot2/bootloader file found in ",
            search_dir,
            ",go on next steps",
        )
        return
    bflb_utils.printf("Copy ", files[0])
    try:
        filedir, ext = os.path.split(imgfile)
        dst_file = os.path.join(search_dir, files[0])
        shutil.copy(dst_file, filedir)
        return os.path.join(filedir, files[0])
    except Exception as e:
        bflb_utils.printf(e)
        bflb_utils.printf("[Warning] Copy boot2/bootloader fail!!!, go on next steps")
        return none


def copy_mfg_file(search_dir, imgfile):
    # search_dir=args.brdcfgdir
    files = found_boot2_mfg_file(search_dir, "mfg")
    if len(files) == 0:
        bflb_utils.printf("[Warning] No mfg file found in ", search_dir, ",go on next steps")
        return
    if len(files) > 1:
        bflb_utils.printf(
            "[Error] More than one mfg file found in ", search_dir, ",go on next steps"
        )
        return
    bflb_utils.printf("Copy ", files[0])
    try:
        filedir, ext = os.path.split(imgfile)
        dst_file = os.path.join(search_dir, files[0])
        shutil.copy(dst_file, filedir)
        return os.path.join(filedir, files[0])
    except Exception as e:
        bflb_utils.printf(e)
        bflb_utils.printf("[Error] Copy mfg fail!!!, go on next steps")
        return None


def firmware_post_process(args, chipname="bl60x"):
    chipname = get_nicky_name(chipname.lower())
    sub_module = __import__("libs." + chipname, fromlist=[chipname])
    sub_module.firmware_post_process_do.firmware_post_proc(args)


def bl60x_mfg_ota_header(chipname, file_bytearray, use_xz):
    header_len = 512
    header = bytearray()
    file_len = len(file_bytearray)
    m = hashlib.sha256()

    # 16 Bytes header
    data = b"BL60X_OTA_Ver1.0"
    # bflb_utils.printf(data.decode('utf-8'))
    for b in data:
        header.append(b)
    # 4 Byte ota file type
    if use_xz:
        data = b"XZ  "
    else:
        data = b"RAW "
    for b in data:
        header.append(b)

    # 4 Bytes file length
    file_len_bytes = file_len.to_bytes(4, byteorder="little")
    for b in file_len_bytes:
        header.append(b)

    # 8 Bytes pad
    header.append(0x01)
    header.append(0x02)
    header.append(0x03)
    header.append(0x04)
    header.append(0x05)
    header.append(0x06)
    header.append(0x07)
    header.append(0x08)

    # 16 Bytes Hardware version
    data = b"BFL_Module_v1.1"  # bytearray(parsed_toml["ota"]["version_hardware"].encode('utf-8'))
    data_len = 16 - len(data)
    for b in data:
        header.append(b)
    while data_len > 0:
        header.append(0x00)
        data_len = data_len - 1

    # 16 Bytes firmware version
    data = b"EVENT_V1.1.1"  # bytearray(parsed_toml["ota"]["version_software"].encode('utf-8'))
    data_len = 16 - len(data)
    for b in data:
        header.append(b)
    while data_len > 0:
        header.append(0x00)
        data_len = data_len - 1

    # 32 Bytes SHA256
    m.update(file_bytearray)
    hash_bytes = m.digest()
    for b in hash_bytes:
        header.append(b)
    header_len = header_len - len(header)
    while header_len > 0:
        header.append(0xFF)
        header_len = header_len - 1
    return header


def firmware_create_ota_file(chipname, fw_file):
    try:
        bl60x_xz_filters = [
            {"id": lzma.FILTER_LZMA2, "dict_size": 32768},
        ]
        with open(fw_file, "rb") as fp:
            fw_raw_data = fp.read()
            fp.close()

        # create .ota file
        ota_file_name = fw_file.replace(".bin", ".bin.ota")
        bflb_utils.printf("create OTA file:", ota_file_name)
        fw_ota_bin_header = bl60x_mfg_ota_header(chipname, fw_raw_data, use_xz=0)
        for b in fw_raw_data:
            fw_ota_bin_header.append(b)
        with open(ota_file_name, "wb+") as fp:
            fp.write(fw_ota_bin_header)
            fp.close()

        # create .xz file
        xz_file_name = fw_file.replace(".bin", ".xz")
        bflb_utils.printf("create XZ file:", xz_file_name)
        with lzma.open(
            xz_file_name, mode="wb", check=lzma.CHECK_CRC32, filters=bl60x_xz_filters
        ) as xz_f:
            xz_f.write(fw_raw_data)
        with open(xz_file_name, mode="rb") as f:
            fw_xz_data = f.read()
            f.close()

        # create .xz.ota file
        xz_ota_file_name = fw_file.replace(".bin", ".xz.ota")
        bflb_utils.printf("create XZ OTA file:", xz_ota_file_name)
        fw_ota_bin_header = bl60x_mfg_ota_header(chipname, fw_xz_data, use_xz=1)
        for b in fw_xz_data:
            fw_ota_bin_header.append(b)
        with open(xz_ota_file_name, "wb+") as fp:
            fp.write(fw_ota_bin_header)
            fp.close()
    except Exception as e:
        bflb_utils.printf(e)
        bflb_utils.printf("[Error] create OTA file fail")
    return False


def encrypt_user_data(args, chipname="bl60x"):
    if args.aeskey == None or args.aesiv == None:
        bflb_utils.printf("[Error] No input key")
        sys.exit()
    if args.xtsmode != None:
        xts_mode = int(args.xtsmode)
    else:
        xts_mode = 0
    encrypt_key = bflb_utils.hexstr_to_bytearray(args.aeskey)
    if len(encrypt_key) != 32 and len(encrypt_key) != 24 and len(encrypt_key) != 16:
        bflb_utils.printf("[Error] Key length error")
        sys.exit()

    iv_value = args.aesiv
    if xts_mode == 1:
        if len(encrypt_key) != 32:
            bflb_utils.printf("[Error] XTS mode key length error")
            sys.exit()
        iv_value = iv_value[24:32] + iv_value[:24]
    encrypt_iv = bflb_utils.hexstr_to_bytearray(iv_value)

    data = bytearray(0)
    with open(args.datafile, "rb") as fp:
        data = fp.read()
    if xts_mode:
        data = img_create_encrypt_data_xts(data, encrypt_key, encrypt_iv, 1)
    else:
        data = img_create_encrypt_data(data, encrypt_key, encrypt_iv, 1)
    with open(args.datafile, "wb+") as fp:
        data = fp.write(data)

    chipname = get_nicky_name(chipname.lower())
    sub_module = __import__("libs." + chipname, fromlist=[chipname])
    sub_module.firmware_post_process_do.add_user_key(args)


def run():
    parser = bflb_utils.firmware_post_proc_parser_init()
    args = parser.parse_args()
    if args.releasenote != True:
        dump_release_note()
        return
    bflb_utils.printf("bflb firmware post process : %s" % version_str)
    # args = parser_image.parse_args("--image=media", "--signer=none")
    bflb_utils.printf("Chipname: %s" % args.chipname)
    if args.aesiv != None:
        if len(args.aesiv) != 32:
            bflb_utils.printf("[Error] AES IV length error")
            return
        if args.aesiv[24:32] != "00000000":
            bflb_utils.printf("[Error] AES IV should end with 00000000")
            return

    if args.chipname.lower() in chip_dict:
        chipname = get_nicky_name(args.chipname.lower())
        if args.checkpartition != None:
            pt_check.dump_partiton(chipname, args.checkpartition)
            return
        if args.datafile != None:
            encrypt_user_data(args, chipname)
            return
        # get image files
        img_file_list = None
        if args.imgfile != None:
            args.imgfile = args.imgfile.replace("'", "").replace('"', "")
            img_file_list = get_img_file_list(args.imgfile, args.chipname, args.cpuid)

        if args.brdcfgdir != None:
            args.brdcfgdir = args.brdcfgdir.replace("'", "").replace('"', "")
            bflb_utils.printf("Board config dir: %s" % args.brdcfgdir)
            create_partiton_table(args.brdcfgdir, img_file_list[0])
            append_dts_file(args.brdcfgdir, img_file_list[0])
            ret = copy_boot2_file(args.brdcfgdir, img_file_list[0])
            if ret != None:
                img_file_list.append(ret)
            ret = copy_mfg_file(args.brdcfgdir, img_file_list[0])
            if ret != None:
                append_dts_file(args.brdcfgdir, ret)
                img_file_list.append(ret)
        # deal files
        for img_file in img_file_list:
            bflb_utils.printf("\r\nProcess ", img_file)
            args.imgfile = img_file
            if parse_header(args.imgfile) == False:
                bflb_utils.printf("[Warning] No boot header found,skip!!!")
                break
            firmware_post_process(args, args.chipname)
        # create ota file,xz file and xz.ota file
        firmware_create_ota_file(args.chipname, img_file_list[0])

    else:
        bflb_utils.printf("[Error] Please set correct chipname config, exit!!!")


if __name__ == "__main__":
    run()
