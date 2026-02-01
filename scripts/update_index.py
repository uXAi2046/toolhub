import re
import json

# Define the new tools metadata (same as in generation script)
TOOLS = [
    {"id": "token-generator", "name": "Token Generator", "name_zh": "Token 生成器", "desc": "Generate random string with custom characters.", "desc_zh": "生成随机字符串。", "category": "Development", "icon": "fa-key"},
    {"id": "hash-text", "name": "Hash Text", "name_zh": "哈希文本", "desc": "Hash text using SHA/MD5.", "desc_zh": "使用 SHA/MD5 哈希文本。", "category": "Development", "icon": "fa-fingerprint"},
    {"id": "bcrypt-generator", "name": "Bcrypt Generator", "name_zh": "Bcrypt 生成器", "desc": "Bcrypt hash generator.", "desc_zh": "Bcrypt 哈希生成。", "category": "Development", "icon": "fa-lock"},
    {"id": "uuid-generator", "name": "UUID Generator", "name_zh": "UUID 生成器", "desc": "Generate UUID v4.", "desc_zh": "生成 UUID v4。", "category": "Development", "icon": "fa-id-card"},
    {"id": "ulid-generator", "name": "ULID Generator", "name_zh": "ULID 生成器", "desc": "Generate ULID.", "desc_zh": "生成 ULID。", "category": "Development", "icon": "fa-arrow-down-1-9"},
    {"id": "encrypt-decrypt", "name": "Encrypt / Decrypt", "name_zh": "加密 / 解密", "desc": "AES/DES encryption.", "desc_zh": "AES/DES 加密。", "category": "Development", "icon": "fa-user-secret"},
    {"id": "bip39-generator", "name": "BIP39 Generator", "name_zh": "BIP39 生成器", "desc": "Mnemonic generator.", "desc_zh": "助记词生成。", "category": "Development", "icon": "fa-book"},
    {"id": "hmac-generator", "name": "HMAC Generator", "name_zh": "HMAC 生成器", "desc": "HMAC calculation.", "desc_zh": "HMAC 计算。", "category": "Development", "icon": "fa-certificate"},
    {"id": "rsa-key-generator", "name": "RSA Key Generator", "name_zh": "RSA 密钥生成", "desc": "Generate RSA keys.", "desc_zh": "生成 RSA 密钥。", "category": "Development", "icon": "fa-key"},
    {"id": "password-strength", "name": "Password Strength", "name_zh": "密码强度", "desc": "Check password strength.", "desc_zh": "检查密码强度。", "category": "Development", "icon": "fa-shield-halved"},
    {"id": "pdf-signature", "name": "PDF Signature", "name_zh": "PDF 签名验证", "desc": "Verify PDF signature.", "desc_zh": "验证 PDF 签名。", "category": "Development", "icon": "fa-file-signature"},
    
    {"id": "integer-converter", "name": "Base Converter", "name_zh": "进制转换", "desc": "Convert number bases.", "desc_zh": "转换数字进制。", "category": "Development", "icon": "fa-calculator"},
    {"id": "case-converter", "name": "Case Converter", "name_zh": "大小写转换", "desc": "Convert string case.", "desc_zh": "转换字符串大小写。", "category": "Development", "icon": "fa-font"},
    {"id": "roman-numeral", "name": "Roman Numeral", "name_zh": "罗马数字", "desc": "Roman to Number.", "desc_zh": "罗马数字转换。", "category": "Development", "icon": "fa-i-cursor"},
    {"id": "yaml-json", "name": "YAML <> JSON", "name_zh": "YAML <> JSON", "desc": "Convert YAML/JSON.", "desc_zh": "YAML/JSON 互转。", "category": "Development", "icon": "fa-file-code"},
    {"id": "list-converter", "name": "List Converter", "name_zh": "列表转换", "desc": "Process lists.", "desc_zh": "处理列表数据。", "category": "Development", "icon": "fa-list"},
    
    {"id": "escape-html", "name": "Escape HTML", "name_zh": "HTML 转义", "desc": "Escape HTML entities.", "desc_zh": "转义 HTML 实体。", "category": "Development", "icon": "fa-code"},
    {"id": "device-info", "name": "Device Info", "name_zh": "设备信息", "desc": "Show device info.", "desc_zh": "显示设备信息。", "category": "Development", "icon": "fa-mobile-screen"},
    {"id": "basic-auth", "name": "Basic Auth", "name_zh": "Basic Auth", "desc": "Generate Basic Auth.", "desc_zh": "生成 Basic Auth。", "category": "Development", "icon": "fa-user-lock"},
    {"id": "otp-generator", "name": "OTP Generator", "name_zh": "OTP 生成器", "desc": "Generate TOTP.", "desc_zh": "生成 TOTP。", "category": "Development", "icon": "fa-stopwatch"},
    {"id": "http-status", "name": "HTTP Status", "name_zh": "HTTP 状态码", "desc": "HTTP status codes.", "desc_zh": "HTTP 状态码列表。", "category": "Development", "icon": "fa-server"},
    {"id": "slugify", "name": "Slugify", "name_zh": "Slug 生成", "desc": "Slugify string.", "desc_zh": "字符串转 Slug。", "category": "Development", "icon": "fa-link"},
    
    {"id": "qr-code", "name": "QR Code", "name_zh": "二维码", "desc": "Generate QR Code.", "desc_zh": "生成二维码。", "category": "Design", "icon": "fa-qrcode"},
    {"id": "wifi-qr", "name": "WiFi QR", "name_zh": "WiFi 二维码", "desc": "Generate WiFi QR.", "desc_zh": "生成 WiFi 二维码。", "category": "Design", "icon": "fa-wifi"},
    {"id": "camera-recorder", "name": "Camera", "name_zh": "摄像头", "desc": "Record video/photo.", "desc_zh": "录制视频/拍照。", "category": "Design", "icon": "fa-camera"},
    
    {"id": "git-cheatsheet", "name": "Git Cheatsheet", "name_zh": "Git 速查表", "desc": "Git commands.", "desc_zh": "Git 命令列表。", "category": "Development", "icon": "fa-code-branch"},
    {"id": "random-port", "name": "Random Port", "name_zh": "随机端口", "desc": "Generate random port.", "desc_zh": "生成随机端口。", "category": "Development", "icon": "fa-shuffle"},
    {"id": "keycode-info", "name": "Keycode Info", "name_zh": "键码信息", "desc": "JS Keycode info.", "desc_zh": "JS 键码信息。", "category": "Development", "icon": "fa-keyboard"}
]

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Prepare Translation Strings
    en_trans = []
    zh_trans = []
    
    for tool in TOOLS:
        key_name = f"tool.{tool['id']}.name"
        key_desc = f"tool.{tool['id']}.desc"
        
        en_trans.append(f"                '{key_name}': '{tool['name']}',")
        en_trans.append(f"                '{key_desc}': '{tool['desc']}',")
        
        zh_trans.append(f"                '{key_name}': '{tool['name_zh']}',")
        zh_trans.append(f"                '{key_desc}': '{tool['desc_zh']}',")

    # 2. Insert Translations
    # Find insertion point for EN (before the closing brace of en object)
    # Looking for 'tool.blockslice.desc': ... }
    # We'll search for the last known key or just before "            },"
    
    content = re.sub(
        r"(^\s+'tool\.blockslice\.desc':.*$)",
        r"\1" + ",\n" + "\n".join(en_trans),
        content,
        flags=re.MULTILINE
    )
    
    # Same for ZH (it's the second block)
    # The zh block ends with 'tool.blockslice.desc': ... }
    # But wait, regex might match the first one again if not careful.
    # Actually, the file structure is:
    # en: { ... },
    # zh: { ... }
    
    # Let's use a specific marker for ZH insertion.
    # The previous regex inserted into EN. Now we need to insert into ZH.
    # The ZH block also has 'tool.blockslice.desc'.
    # Since we already modified the first one, the first one is now followed by our new keys.
    # So we can search for 'tool.blockslice.desc' again, but we need to target the second occurrence?
    # No, that's risky.
    
    # Let's read the file again or handle it differently.
    # Actually, let's just find "zh: {" and then find the end of that block.
    
    # Better approach: Read file, split by lines, find markers.
    lines = content.split('\n')
    new_lines = []
    
    in_en = False
    in_zh = False
    en_done = False
    zh_done = False
    
    last_id = 25 # Based on known file content
    
    tool_objects = []
    
    for tool in TOOLS:
        last_id += 1
        obj = f"""            {{
                id: {last_id},
                nameKey: "tool.{tool['id']}.name",
                descKey: "tool.{tool['id']}.desc",
                vendor: "Tool Center",
                category: "{tool['category']}",
                categoryStyle: "bg-blue-50 text-blue-700",
                meta: "v1.0.0",
                icon: "{tool['icon']}",
                iconColor: "text-blue-600",
                logoBg: "bg-blue-50",
                link: "{tool['id']}.html"
            }}"""
        tool_objects.append(obj)
        
    tools_str = ",\n".join(tool_objects)

    # Re-read fresh content to avoid confusion from previous regex attempt (which I haven't run yet)
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    final_lines = []
    for line in lines:
        # Insert EN translations
        if "'tool.blockslice.desc'" in line and "Split images" in line and not en_done:
            final_lines.append(line.rstrip() + ",\n")
            final_lines.append("\n".join(en_trans) + "\n")
            en_done = True
            continue
            
        # Insert ZH translations
        if "'tool.blockslice.desc'" in line and "网格帖子" in line and not zh_done:
            final_lines.append(line.rstrip() + ",\n")
            final_lines.append("\n".join(zh_trans) + "\n")
            zh_done = True
            continue
            
        # Insert Tools
        if "id: 25," in line: # Found the last tool start
             pass
        
        if "link: \"https://traememe-cutrz6l.vercel.app/\"" in line:
            final_lines.append(line)
            final_lines.append("            },\n")
            final_lines.append(tools_str)
            # Skip the next line which is likely "        ];" or "            }"
            # Actually, let's just insert before "        ];"
            continue
            
        if "        ];" in line and "const tools" not in line: # End of tools array
             # If we inserted above, we don't need to do anything here except append the line
             pass

        final_lines.append(line)

    # The previous logic for tools insertion is a bit flaky. Let's fix it.
    # We want to insert BEFORE "        ];"
    
    final_lines = []
    for line in lines:
        if "        ];" in line:
            # Check if we already inserted? No.
            # We append the comma to previous item if needed?
            # The previous item (id 25) block ends with "            }".
            # So we should replace "            }" with "            }," and then append our tools.
            pass
            
    # Let's try a simpler regex approach for the whole file.
    content = "".join(lines)
    
    # 1. Inject EN
    # Look for the EN block slice desc line
    content = re.sub(
        r"('tool\.blockslice\.desc': 'Split images[^']+')", 
        r"\1,\n" + "\n".join(en_trans), 
        content
    )
    
    # 2. Inject ZH
    # Look for the ZH block slice desc line (contains Chinese)
    content = re.sub(
        r"('tool\.blockslice\.desc': '将图片分割成[^']+')", 
        r"\1,\n" + "\n".join(zh_trans), 
        content
    )
    
    # 3. Inject Tools
    # Look for the closing of the last tool (id 25)
    # It ends with link: "..." }
    # We replace "}" with "}," and add new tools
    
    # Construct the tools string to be valid JS objects
    tools_js = ",\n".join(tool_objects)
    
    # Find the end of tools array
    # The last tool is blockslice.
    pattern = r"(link: \"https://traememe-cutrz6l.vercel.app/\"\s+})"
    content = re.sub(
        pattern,
        r"\1,\n" + tools_js,
        content
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Index updated successfully.")

if __name__ == '__main__':
    update_index()
