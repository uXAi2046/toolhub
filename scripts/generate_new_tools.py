import os
import json

# ==========================================
# 1. Tool Definitions
# ==========================================

TOOLS = [
    # --- Crypto & Security ---
    {
        "id": "token-generator",
        "name": "Token Generator",
        "name_zh": "Token 生成器",
        "desc": "Generate random string with custom characters, uppercase/lowercase, numbers, and symbols.",
        "desc_zh": "生成包含自定义字符、大小写字母、数字和符号的随机字符串。",
        "category": "Crypto & Security",
        "icon": "fa-key",
        "type": "generator",
        "logic_type": "token"
    },
    {
        "id": "hash-text",
        "name": "Hash Text",
        "name_zh": "哈希文本",
        "desc": "Hash text using algorithms like SHA1, SHA256, SHA512, SHA3, RIPEMD160.",
        "desc_zh": "使用 SHA1, SHA256, SHA512, RIPEMD160 等算法进行哈希。",
        "category": "Crypto & Security",
        "icon": "fa-fingerprint",
        "type": "converter",
        "logic_type": "hash",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"]
    },
    {
        "id": "bcrypt-generator",
        "name": "Bcrypt Generator",
        "name_zh": "Bcrypt 生成器",
        "desc": "Hash and compare text strings using the Bcrypt password-hashing function.",
        "desc_zh": "使用 Bcrypt 算法对字符串进行哈希处理和验证。",
        "category": "Crypto & Security",
        "icon": "fa-lock",
        "type": "converter",
        "logic_type": "bcrypt",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/bcryptjs/2.4.3/bcrypt.min.js"]
    },
    {
        "id": "uuid-generator",
        "name": "UUID Generator",
        "name_zh": "UUID 生成器",
        "desc": "Generate Universally Unique Identifiers (UUIDs) version 4.",
        "desc_zh": "生成版本 4 的通用唯一识别码 (UUID)。",
        "category": "Crypto & Security",
        "icon": "fa-id-card",
        "type": "generator",
        "logic_type": "uuid"
    },
    {
        "id": "ulid-generator",
        "name": "ULID Generator",
        "name_zh": "ULID 生成器",
        "desc": "Generate Universally Unique Lexicographically Sortable Identifiers (ULID).",
        "desc_zh": "生成按字典顺序排序的通用唯一识别码 (ULID)。",
        "category": "Crypto & Security",
        "icon": "fa-arrow-down-1-9",
        "type": "generator",
        "logic_type": "ulid",
        "libs": ["https://unpkg.com/ulid@2.3.0/dist/index.umd.js"]
    },
    {
        "id": "encrypt-decrypt",
        "name": "Encrypt / Decrypt",
        "name_zh": "加密 / 解密",
        "desc": "Encrypt and decrypt text using algorithms like AES, TripleDES, Rabbit, or RC4.",
        "desc_zh": "使用 AES, TripleDES, RC4 等算法加密和解密文本。",
        "category": "Crypto & Security",
        "icon": "fa-user-secret",
        "type": "converter",
        "logic_type": "encrypt",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"]
    },
     {
        "id": "bip39-generator",
        "name": "BIP39 Generator",
        "name_zh": "BIP39 生成器",
        "desc": "Generate a BIP39 passphrase from a mnemonic or vice-versa.",
        "desc_zh": "生成 BIP39 助记词或从助记词生成密码短语。",
        "category": "Crypto & Security",
        "icon": "fa-book",
        "type": "coming_soon"
    },
    {
        "id": "hmac-generator",
        "name": "HMAC Generator",
        "name_zh": "HMAC 生成器",
        "desc": "Compute Hash-based Message Authentication Code (HMAC) using a secret key.",
        "desc_zh": "使用密钥计算基于哈希的消息认证码 (HMAC)。",
        "category": "Crypto & Security",
        "icon": "fa-certificate",
        "type": "converter",
        "logic_type": "hmac",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"]
    },
    {
        "id": "rsa-key-generator",
        "name": "RSA Key Generator",
        "name_zh": "RSA 密钥生成",
        "desc": "Generate new random RSA private and public PEM certificate key pairs.",
        "desc_zh": "生成新的随机 RSA 公钥和私钥对 (PEM 格式)。",
        "category": "Crypto & Security",
        "icon": "fa-key",
        "type": "generator",
        "logic_type": "rsa",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/jsencrypt/3.3.2/jsencrypt.min.js"]
    },
    {
        "id": "password-strength",
        "name": "Password Strength",
        "name_zh": "密码强度分析",
        "desc": "Analyze the strength of a password and estimate crack time.",
        "desc_zh": "分析密码强度并估算破解所需时间。",
        "category": "Crypto & Security",
        "icon": "fa-shield-halved",
        "type": "converter",
        "logic_type": "password_strength",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/zxcvbn/4.4.2/zxcvbn.js"]
    },

    {
        "id": "pdf-signature",
        "name": "PDF Signature",
        "name_zh": "PDF 签名验证",
        "desc": "Verify signatures in a PDF file.",
        "desc_zh": "验证 PDF 文件签名。",
        "category": "Crypto & Security",
        "icon": "fa-file-signature",
        "type": "coming_soon"
    },

    # --- Converters ---
    {
        "id": "integer-converter",
        "name": "Base Converter",
        "name_zh": "进制转换",
        "desc": "Convert numbers between different bases (decimal, hexadecimal, binary, octal).",
        "desc_zh": "在十进制、十六进制、二进制、八进制等进制间转换数字。",
        "category": "Converters",
        "icon": "fa-calculator",
        "type": "converter",
        "logic_type": "base_converter"
    },
    {
        "id": "case-converter",
        "name": "Case Converter",
        "name_zh": "大小写转换",
        "desc": "Transform string case (uppercase, lowercase, camelCase, snake_case, etc.).",
        "desc_zh": "转换字符串的大小写格式 (如 camelCase, snake_case 等)。",
        "category": "Converters",
        "icon": "fa-font",
        "type": "converter",
        "logic_type": "case_converter",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js"]
    },
    {
        "id": "roman-numeral",
        "name": "Roman Numeral",
        "name_zh": "罗马数字转换",
        "desc": "Convert Roman numerals to numbers and vice-versa.",
        "desc_zh": "罗马数字与阿拉伯数字互转。",
        "category": "Converters",
        "icon": "fa-i-cursor",
        "type": "converter",
        "logic_type": "roman"
    },
    {
        "id": "yaml-json",
        "name": "YAML <> JSON",
        "name_zh": "YAML <> JSON",
        "desc": "Convert YAML to JSON and JSON to YAML.",
        "desc_zh": "YAML 与 JSON 格式互转。",
        "category": "Converters",
        "icon": "fa-file-code",
        "type": "converter",
        "logic_type": "yaml_json",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js"]
    },
     {
        "id": "list-converter",
        "name": "List Converter",
        "name_zh": "列表转换",
        "desc": "Process column-based data (transpose, reverse, sort, truncate).",
        "desc_zh": "处理列表数据（转置、排序、反转、截断、去重等）。",
        "category": "Converters",
        "icon": "fa-list",
        "type": "converter",
        "logic_type": "list_converter"
    },

    # --- Web & Network ---
    {
        "id": "escape-html",
        "name": "Escape HTML",
        "name_zh": "HTML 转义",
        "desc": "Escape or unescape HTML entities.",
        "desc_zh": "转义或反转义 HTML 实体字符。",
        "category": "Web & Network",
        "icon": "fa-code",
        "type": "converter",
        "logic_type": "escape_html"
    },
    {
        "id": "device-info",
        "name": "Device Info",
        "name_zh": "设备信息",
        "desc": "Get information about the current device (screen size, user agent).",
        "desc_zh": "获取当前设备信息 (屏幕尺寸、像素比、User Agent 等)。",
        "category": "Web & Network",
        "icon": "fa-mobile-screen",
        "type": "info",
        "logic_type": "device_info"
    },
    {
        "id": "basic-auth",
        "name": "Basic Auth Gen",
        "name_zh": "Basic Auth 生成",
        "desc": "Generate a base64 basic auth header from a username and password.",
        "desc_zh": "根据用户名和密码生成 Base64 编码的 Basic Auth 请求头。",
        "category": "Web & Network",
        "icon": "fa-user-lock",
        "type": "generator",
        "logic_type": "basic_auth"
    },
    {
        "id": "otp-generator",
        "name": "OTP Generator",
        "name_zh": "OTP 生成器",
        "desc": "Generate and validate time-based OTP for multi-factor authentication.",
        "desc_zh": "生成和验证基于时间的一次性密码 (TOTP)。",
        "category": "Web & Network",
        "icon": "fa-stopwatch",
        "type": "coming_soon"
    },
     {
        "id": "http-status",
        "name": "HTTP Status",
        "name_zh": "HTTP 状态码",
        "desc": "List of all HTTP status codes, their names, and meanings.",
        "desc_zh": "查询 HTTP 状态码列表及其含义。",
        "category": "Web & Network",
        "icon": "fa-server",
        "type": "info",
        "logic_type": "http_status"
    },
    {
        "id": "slugify",
        "name": "Slugify String",
        "name_zh": "Slug 生成",
        "desc": "Make a string URL, filename, and ID safe.",
        "desc_zh": "将字符串转换为 URL 安全的格式 (Slug)。",
        "category": "Web & Network",
        "icon": "fa-link",
        "type": "converter",
        "logic_type": "slugify"
    },

    # --- Images ---
    {
        "id": "qr-code",
        "name": "QR Code Generator",
        "name_zh": "二维码生成",
        "desc": "Generate and download QR codes for URLs or text.",
        "desc_zh": "生成自定义颜色和内容的二维码。",
        "category": "Images & Media",
        "icon": "fa-qrcode",
        "type": "generator",
        "logic_type": "qrcode",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"]
    },
    {
        "id": "wifi-qr",
        "name": "WiFi QR Code",
        "name_zh": "WiFi 二维码",
        "desc": "Generate QR codes for quick connections to WiFi networks.",
        "desc_zh": "生成用于快速连接 WiFi 的二维码。",
        "category": "Images & Media",
        "icon": "fa-wifi",
        "type": "generator",
        "logic_type": "wifi_qr",
        "libs": ["https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"]
    },
     {
        "id": "camera-recorder",
        "name": "Camera Recorder",
        "name_zh": "摄像头录制",
        "desc": "Take a picture or record a video from your webcam or camera.",
        "desc_zh": "调用摄像头拍照或录制视频。",
        "category": "Images & Media",
        "icon": "fa-camera",
        "type": "interactive",
        "logic_type": "camera"
    },

    # --- Development ---
    {
        "id": "git-cheatsheet",
        "name": "Git Cheatsheet",
        "name_zh": "Git 速查表",
        "desc": "Quick access to common git commands.",
        "desc_zh": "常用 Git 命令速查表。",
        "category": "Development",
        "icon": "fa-code-branch",
        "type": "info",
        "logic_type": "git_cheatsheet"
    },
    {
        "id": "random-port",
        "name": "Random Port",
        "name_zh": "随机端口",
        "desc": "Generate random port numbers outside of the range of known ports.",
        "desc_zh": "生成常用端口范围之外的随机端口号。",
        "category": "Development",
        "icon": "fa-shuffle",
        "type": "generator",
        "logic_type": "random_port"
    },
    {
        "id": "keycode-info",
        "name": "Keycode Info",
        "name_zh": "键码信息",
        "desc": "Find the javascript keycode, code, location and modifiers of any pressed key.",
        "desc_zh": "获取按键的 JavaScript keyCode、code 和 location 信息。",
        "category": "Development",
        "icon": "fa-keyboard",
        "type": "interactive",
        "logic_type": "keycode"
    }
]


# ==========================================
# 2. Logic Snippets (JavaScript)
# ==========================================

LOGIC_TEMPLATES = {
    "token": """
        function generate() {
            const length = 32;
            const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*';
            let result = '';
            for (let i = 0; i < length; i++) {
                result += chars.charAt(Math.floor(Math.random() * chars.length));
            }
            document.getElementById('output').value = result;
            showToast('Token Generated', 'success');
        }
        // Auto generate on load
        window.addEventListener('DOMContentLoaded', generate);
    """,
    "uuid": """
        function generate() {
            const uuid = crypto.randomUUID();
            document.getElementById('output').value = uuid;
            showToast('UUID Generated', 'success');
        }
        window.addEventListener('DOMContentLoaded', generate);
    """,
    "hash": """
        function process() {
            const input = document.getElementById('input').value;
            if(!input) return;
            
            const alg = document.getElementById('option-select').value;
            let result = '';
            
            if(alg === 'MD5') result = CryptoJS.MD5(input).toString();
            else if(alg === 'SHA1') result = CryptoJS.SHA1(input).toString();
            else if(alg === 'SHA256') result = CryptoJS.SHA256(input).toString();
            else if(alg === 'SHA512') result = CryptoJS.SHA512(input).toString();
            else if(alg === 'RIPEMD160') result = CryptoJS.RIPEMD160(input).toString();
            
            document.getElementById('output').value = result;
        }
    """,
    "bcrypt": """
        function process() {
            const input = document.getElementById('input').value;
            if(!input) return;
            const salt = dcodeIO.bcrypt.genSaltSync(10);
            const hash = dcodeIO.bcrypt.hashSync(input, salt);
            document.getElementById('output').value = hash;
        }
    """,
    "encrypt": """
        function process() {
            const input = document.getElementById('input').value;
            const pass = document.getElementById('pass-input').value;
            if(!input || !pass) { showToast('Input and Password required', 'error'); return; }
            
            const mode = document.getElementById('mode-select').value; // encrypt/decrypt
            let result = '';
            
            try {
                if(mode === 'encrypt') {
                    result = CryptoJS.AES.encrypt(input, pass).toString();
                } else {
                    const bytes = CryptoJS.AES.decrypt(input, pass);
                    result = bytes.toString(CryptoJS.enc.Utf8);
                }
                document.getElementById('output').value = result;
            } catch(e) {
                document.getElementById('output').value = 'Error: ' + e.message;
            }
        }
    """,
    "case_converter": """
        function process() {
            const input = document.getElementById('input').value;
            const mode = document.getElementById('option-select').value;
            let result = input;
            
            if(mode === 'upper') result = input.toUpperCase();
            else if(mode === 'lower') result = input.toLowerCase();
            else if(mode === 'camel') result = _.camelCase(input);
            else if(mode === 'kebab') result = _.kebabCase(input);
            else if(mode === 'snake') result = _.snakeCase(input);
            else if(mode === 'start') result = _.startCase(input);
            
            document.getElementById('output').value = result;
        }
    """,
    "base_converter": """
        function process() {
            const input = document.getElementById('input').value;
            const fromBase = parseInt(document.getElementById('from-base').value);
            const toBase = parseInt(document.getElementById('to-base').value);
            
            try {
                const val = parseInt(input, fromBase);
                if(isNaN(val)) throw new Error('Invalid input');
                document.getElementById('output').value = val.toString(toBase).toUpperCase();
            } catch(e) {
                document.getElementById('output').value = 'Error';
            }
        }
    """,
    "slugify": """
        function process() {
            const input = document.getElementById('input').value;
            const slug = input.toLowerCase()
                .trim()
                .replace(/[^\w\s-]/g, '')
                .replace(/[\s_-]+/g, '-')
                .replace(/^-+|-+$/g, '');
            document.getElementById('output').value = slug;
        }
    """,
    "qrcode": """
        let qr = null;
        function generate() {
            const input = document.getElementById('input').value;
            const container = document.getElementById('qr-container');
            container.innerHTML = '';
            
            if(!input) return;
            
            new QRCode(container, {
                text: input,
                width: 256,
                height: 256,
                colorDark : "#000000",
                colorLight : "#ffffff",
                correctLevel : QRCode.CorrectLevel.H
            });
        }
    """,
    "wifi_qr": """
        function generate() {
            const ssid = document.getElementById('ssid').value;
            const pass = document.getElementById('pass').value;
            const type = document.getElementById('type').value;
            const hidden = document.getElementById('hidden').checked;
            
            if(!ssid) return;
            
            const wifiStr = `WIFI:T:${type};S:${ssid};P:${pass};H:${hidden};;`;
            
            const container = document.getElementById('qr-container');
            container.innerHTML = '';
            
            new QRCode(container, {
                text: wifiStr,
                width: 256,
                height: 256
            });
        }
    """,
    "random_port": """
        function generate() {
            const count = 10;
            let ports = [];
            for(let i=0; i<count; i++) {
                // Ports > 1024 and < 65535
                ports.push(Math.floor(Math.random() * (65535 - 1024 + 1)) + 1024);
            }
            document.getElementById('output').value = ports.join('\\n');
        }
        window.addEventListener('DOMContentLoaded', generate);
    """,
     "roman": """
        function process() {
            const input = document.getElementById('input').value.toUpperCase();
            const lookup = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1};
            
            // Detect if number or roman
            if(/^[0-9]+$/.test(input)) {
                let num = parseInt(input);
                let roman = '';
                for ( let i in lookup ) {
                    while ( num >= lookup[i] ) {
                        roman += i;
                        num -= lookup[i];
                    }
                }
                document.getElementById('output').value = roman;
            } else {
                let num = 0;
                let str = input;
                for ( let i in lookup ) {
                    while ( str.indexOf(i) === 0 ) {
                        num += lookup[i];
                        str = str.replace(i,'');
                    }
                }
                document.getElementById('output').value = num || 'Invalid Roman Numeral';
            }
        }
    """,
    "list_converter": """
        function process() {
            const input = document.getElementById('input').value;
            const mode = document.getElementById('option-select').value;
            let lines = input.split('\\n');
            
            if(mode === 'sort') lines.sort();
            else if(mode === 'reverse') lines.reverse();
            else if(mode === 'unique') lines = [...new Set(lines)];
            else if(mode === 'trim') lines = lines.map(l => l.trim());
            else if(mode === 'number') lines = lines.map((l, i) => `${i+1}. ${l}`);
            
            document.getElementById('output').value = lines.join('\\n');
        }
    """,
    "escape_html": """
        function process() {
            const input = document.getElementById('input').value;
            const mode = document.getElementById('mode-select').value;
            
            if(mode === 'escape') {
                 document.getElementById('output').value = input
                    .replace(/&/g, "&amp;")
                    .replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;")
                    .replace(/"/g, "&quot;")
                    .replace(/'/g, "&#039;");
            } else {
                 document.getElementById('output').value = input
                    .replace(/&amp;/g, "&")
                    .replace(/&lt;/g, "<")
                    .replace(/&gt;/g, ">")
                    .replace(/&quot;/g, '"')
                    .replace(/&#039;/g, "'");
            }
        }
    """,
    "basic_auth": """
        function generate() {
            const user = document.getElementById('user').value;
            const pass = document.getElementById('pass').value;
            if(!user) return;
            const token = btoa(user + ':' + pass);
            document.getElementById('output').value = 'Authorization: Basic ' + token;
        }
    """,
    "http_status": """
        // Static info, no logic needed for v1
    """,
    "git_cheatsheet": """
        // Static info
    """,
    "device_info": """
        window.addEventListener('DOMContentLoaded', () => {
            const info = [
                `User Agent: ${navigator.userAgent}`,
                `Screen: ${window.screen.width} x ${window.screen.height}`,
                `Window: ${window.innerWidth} x ${window.innerHeight}`,
                `Pixel Ratio: ${window.devicePixelRatio}`,
                `Platform: ${navigator.platform}`,
                `Language: ${navigator.language}`,
                `Cookies Enabled: ${navigator.cookieEnabled}`,
                `Cores: ${navigator.hardwareConcurrency || 'Unknown'}`
            ].join('\\n');
            document.getElementById('output').value = info;
        });
    """,
    "keycode": """
        window.addEventListener('keydown', (e) => {
            document.getElementById('key-display').textContent = e.key === ' ' ? 'Space' : e.key;
            document.getElementById('code-display').textContent = e.code;
            document.getElementById('which-display').textContent = e.which;
            document.getElementById('location-display').textContent = e.location;
            
            e.preventDefault();
        });
    """
}

# ==========================================
# 3. HTML Templates
# ==========================================

def get_html(tool, lang='en'):
    is_zh = lang == 'zh'
    t_name = tool['name_zh'] if is_zh else tool['name']
    t_desc = tool['desc_zh'] if is_zh else tool['desc']
    t_cat = tool.get('category', 'Development')
    
    # Common Head
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t_name} - Tool Center</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    {''.join([f'<script src="{lib}"></script>' for lib in tool.get('libs', [])])}
    <style>
        body {{ font-family: 'Inter', sans-serif; background-color: #F9FAFB; }}
    </style>
</head>
<body class="text-slate-900 antialiased min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-white border-b border-gray-100 sticky top-0 z-50">
        <div class="max-w-[1400px] mx-auto px-6 h-16 flex items-center">
            <a href="index.html" class="flex items-center gap-3 cursor-pointer">
                <div class="grid grid-cols-2 gap-0.5 w-6 h-6">
                    <div class="bg-blue-600 rounded-[1px]"></div>
                    <div class="bg-blue-600 rounded-[1px]"></div>
                    <div class="bg-blue-600 rounded-[1px]"></div>
                    <div class="bg-blue-600 rounded-[1px] opacity-50"></div>
                </div>
                <span class="font-bold text-lg tracking-tight text-gray-900">Tool Center</span>
            </a>
        </div>
    </header>

    <main class="flex-grow max-w-[1400px] mx-auto px-6 py-8 w-full">
        <div class="mb-6 flex items-center text-sm text-gray-500">
            <a href="index.html" class="hover:text-blue-600 transition-colors flex items-center gap-2">
                <i class="fa-solid fa-house"></i> Home
            </a>
            <i class="fa-solid fa-chevron-right text-xs mx-3 text-gray-300"></i>
            <span class="font-medium text-gray-900">{t_name}</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-8 space-y-6">
                <div>
                    <h1 class="text-3xl font-bold text-gray-900 mb-3">{t_name}</h1>
                    <p class="text-gray-500 leading-relaxed">{t_desc}</p>
                </div>

                <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden p-6">
                    {get_tool_body(tool, lang)}
                </div>
            </div>

            <!-- Sidebar -->
            <div class="lg:col-span-4 space-y-6">
                <div class="bg-white rounded-xl border border-gray-200 p-6 shadow-sm">
                    <h3 class="font-bold text-gray-900 mb-4">About</h3>
                    <p class="text-sm text-gray-500 mb-6 leading-relaxed">
                        {t_desc}
                    </p>
                    <div class="flex justify-between text-sm">
                        <span class="text-gray-500">Category</span>
                        <span class="font-medium text-gray-900">{t_cat}</span>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script>
        // Toast
        function showToast(message, type = 'success') {{
            let container = document.getElementById('toast-container');
            if (!container) {{
                container = document.createElement('div');
                container.id = 'toast-container';
                container.className = 'fixed bottom-5 right-5 flex flex-col gap-3 z-50';
                document.body.appendChild(container);
            }}
            const toast = document.createElement('div');
            const bgColor = type === 'success' ? 'bg-green-600' : 'bg-red-600';
            toast.className = `${{bgColor}} text-white px-4 py-3 rounded-lg shadow-lg text-sm font-medium flex items-center gap-2 transform transition-all duration-300 translate-y-10 opacity-0`;
            toast.innerHTML = `<i class="fa-solid ${{type === 'success' ? 'fa-circle-check' : 'fa-circle-exclamation'}}"></i> ${{message}}`;
            container.appendChild(toast);
            requestAnimationFrame(() => toast.classList.remove('translate-y-10', 'opacity-0'));
            setTimeout(() => {{
                toast.classList.add('opacity-0', 'translate-y-2');
                setTimeout(() => toast.remove(), 300);
            }}, 3000);
        }}

        function copyResult() {{
            const output = document.getElementById('output');
            if (!output || !output.value) return;
            navigator.clipboard.writeText(output.value).then(() => showToast('Copied to clipboard'));
        }}

        {get_tool_js(tool)}
    </script>
</body>
</html>
"""
    return html

def get_tool_body(tool, lang):
    t_type = tool.get('type')
    logic = tool.get('logic_type', '')
    
    if t_type == 'coming_soon':
        return """
        <div class="text-center py-12">
            <i class="fa-solid fa-person-digging text-4xl text-blue-200 mb-4"></i>
            <h3 class="text-lg font-bold text-gray-900">Coming Soon</h3>
            <p class="text-gray-500">This tool is currently under development.</p>
        </div>
        """
        
    if logic == 'qrcode' or logic == 'wifi_qr':
        inputs = ""
        if logic == 'wifi_qr':
            inputs = """
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <input type="text" id="ssid" placeholder="Network Name (SSID)" class="w-full p-3 border rounded-lg" oninput="generate()">
                <input type="text" id="pass" placeholder="Password" class="w-full p-3 border rounded-lg" oninput="generate()">
                <select id="type" class="w-full p-3 border rounded-lg" onchange="generate()">
                    <option value="WPA">WPA/WPA2</option>
                    <option value="WEP">WEP</option>
                    <option value="nopass">No Password</option>
                </select>
                <div class="flex items-center">
                    <input type="checkbox" id="hidden" class="mr-2" onchange="generate()"> <label>Hidden Network</label>
                </div>
            </div>
            """
        else:
            inputs = """<input type="text" id="input" placeholder="Enter text or URL" class="w-full p-3 border rounded-lg mb-4" oninput="generate()">"""
            
        return f"""
        {inputs}
        <div id="qr-container" class="flex justify-center p-6 bg-white border rounded-lg"></div>
        """

    if logic == 'keycode':
        return """
        <div class="text-center py-12">
            <h2 class="text-6xl font-bold text-blue-600 mb-4" id="key-display">Press any key</h2>
            <div class="grid grid-cols-3 gap-4 max-w-lg mx-auto mt-8">
                <div class="p-4 bg-gray-50 rounded-lg"><div class="text-xs text-gray-500">event.code</div><div class="text-xl font-mono font-bold" id="code-display">-</div></div>
                <div class="p-4 bg-gray-50 rounded-lg"><div class="text-xs text-gray-500">event.which</div><div class="text-xl font-mono font-bold" id="which-display">-</div></div>
                <div class="p-4 bg-gray-50 rounded-lg"><div class="text-xs text-gray-500">event.location</div><div class="text-xl font-mono font-bold" id="location-display">-</div></div>
            </div>
        </div>
        """

    if logic == 'camera':
        return """
        <div class="space-y-4">
            <div class="aspect-video bg-black rounded-lg overflow-hidden relative">
                <video id="video" class="w-full h-full object-cover" autoplay playsinline></video>
            </div>
            <div class="flex justify-center gap-4">
                <button onclick="startCamera()" class="px-6 py-2 bg-blue-600 text-white rounded-lg">Start Camera</button>
                <button onclick="takePhoto()" class="px-6 py-2 bg-white border border-gray-300 rounded-lg">Take Photo</button>
            </div>
            <canvas id="canvas" class="hidden"></canvas>
            <img id="photo" class="w-full rounded-lg hidden border border-gray-200">
        </div>
        """

    # Default Converter/Generator Layout
    controls = ""
    if logic == 'hash':
        controls = """
        <select id="option-select" class="p-2 border rounded" onchange="process()">
            <option value="MD5">MD5</option>
            <option value="SHA1">SHA1</option>
            <option value="SHA256" selected>SHA256</option>
            <option value="SHA512">SHA512</option>
            <option value="RIPEMD160">RIPEMD160</option>
        </select>
        """
    elif logic == 'case_converter':
        controls = """
        <select id="option-select" class="p-2 border rounded" onchange="process()">
            <option value="upper">UPPERCASE</option>
            <option value="lower">lowercase</option>
            <option value="camel">camelCase</option>
            <option value="kebab">kebab-case</option>
            <option value="snake">snake_case</option>
            <option value="start">Capitalize Words</option>
        </select>
        """
    elif logic == 'base_converter':
        controls = """
        <div class="flex gap-2">
            <select id="from-base" class="p-2 border rounded">
                <option value="10">Decimal (10)</option>
                <option value="16">Hex (16)</option>
                <option value="2">Binary (2)</option>
                <option value="8">Octal (8)</option>
            </select>
            <span class="self-center">to</span>
            <select id="to-base" class="p-2 border rounded">
                <option value="16">Hex (16)</option>
                <option value="10">Decimal (10)</option>
                <option value="2">Binary (2)</option>
                <option value="8">Octal (8)</option>
            </select>
        </div>
        <button onclick="process()" class="px-4 py-2 bg-blue-600 text-white rounded">Convert</button>
        """
    elif logic == 'encrypt':
         controls = """
         <input type="text" id="pass-input" placeholder="Secret Key" class="p-2 border rounded flex-grow">
         <select id="mode-select" class="p-2 border rounded">
            <option value="encrypt">Encrypt</option>
            <option value="decrypt">Decrypt</option>
         </select>
         <button onclick="process()" class="px-4 py-2 bg-blue-600 text-white rounded">Go</button>
         """
    if logic == 'escape_html':
        controls = """
        <select id="mode-select" class="p-2 border rounded" onchange="process()">
            <option value="escape">Escape</option>
            <option value="unescape">Unescape</option>
        </select>
        """
    elif logic == 'list_converter':
        controls = """
        <select id="option-select" class="p-2 border rounded" onchange="process()">
            <option value="sort">Sort A-Z</option>
            <option value="reverse">Reverse</option>
            <option value="unique">Remove Duplicates</option>
            <option value="trim">Trim Whitespace</option>
            <option value="number">Add Numbers</option>
        </select>
        """
    elif logic == 'basic_auth':
        controls = "" # Override default
        # Custom input area for basic auth
        input_area = """
        <div class="grid grid-cols-2 gap-4 mb-4">
            <input type="text" id="user" placeholder="Username" class="p-3 border rounded-lg" oninput="generate()">
            <input type="text" id="pass" placeholder="Password" class="p-3 border rounded-lg" oninput="generate()">
        </div>
        """
    elif logic == 'http_status':
        return """
        <div class="overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th class="px-6 py-3">Code</th>
                        <th class="px-6 py-3">Status</th>
                        <th class="px-6 py-3">Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-green-600">200</td><td class="px-6 py-4">OK</td><td class="px-6 py-4">Standard response for successful requests.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-green-600">201</td><td class="px-6 py-4">Created</td><td class="px-6 py-4">Resource has been created.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-blue-600">301</td><td class="px-6 py-4">Moved Permanently</td><td class="px-6 py-4">URL has changed permanently.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-orange-600">400</td><td class="px-6 py-4">Bad Request</td><td class="px-6 py-4">Server cannot process request due to client error.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-orange-600">401</td><td class="px-6 py-4">Unauthorized</td><td class="px-6 py-4">Authentication is required.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-orange-600">403</td><td class="px-6 py-4">Forbidden</td><td class="px-6 py-4">Server refuses to authorize request.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-orange-600">404</td><td class="px-6 py-4">Not Found</td><td class="px-6 py-4">Resource not found.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-red-600">500</td><td class="px-6 py-4">Internal Server Error</td><td class="px-6 py-4">Generic server error.</td></tr>
                    <tr class="bg-white border-b"><td class="px-6 py-4 font-bold text-red-600">502</td><td class="px-6 py-4">Bad Gateway</td><td class="px-6 py-4">Invalid response from upstream server.</td></tr>
                </tbody>
            </table>
        </div>
        """
    elif logic == 'git_cheatsheet':
        return """
        <div class="space-y-4">
            <div class="bg-gray-50 p-4 rounded-lg">
                <h3 class="font-bold text-gray-900 mb-2">Configuration</h3>
                <code class="block text-sm text-blue-600">git config --global user.name "Name"</code>
                <code class="block text-sm text-blue-600">git config --global user.email "email"</code>
            </div>
            <div class="bg-gray-50 p-4 rounded-lg">
                <h3 class="font-bold text-gray-900 mb-2">Starting</h3>
                <code class="block text-sm text-blue-600">git init</code>
                <code class="block text-sm text-blue-600">git clone [url]</code>
            </div>
             <div class="bg-gray-50 p-4 rounded-lg">
                <h3 class="font-bold text-gray-900 mb-2">Changes</h3>
                <code class="block text-sm text-blue-600">git status</code>
                <code class="block text-sm text-blue-600">git add .</code>
                <code class="block text-sm text-blue-600">git commit -m "message"</code>
            </div>
        </div>
        """

    elif t_type == 'generator':
        controls = """<button onclick="generate()" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Generate</button>"""
    elif t_type == 'converter':
        controls = """<button onclick="process()" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">Process</button>"""

    input_area = ""
    if t_type == 'converter' or logic in ['hash', 'bcrypt', 'slugify']:
         input_area = """
         <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700 mb-1">Input</label>
            <textarea id="input" class="w-full h-32 p-3 border border-gray-300 rounded-lg font-mono text-sm" placeholder="Paste content here..."></textarea>
         </div>
         """
    
    output_area = """
    <div class="mt-4">
        <label class="block text-sm font-medium text-gray-700 mb-1">Result</label>
        <div class="relative">
            <textarea id="output" readonly class="w-full h-32 p-3 bg-gray-50 border border-gray-300 rounded-lg font-mono text-sm" placeholder="Result will appear here..."></textarea>
            <button onclick="copyResult()" class="absolute top-2 right-2 text-gray-400 hover:text-blue-600">
                <i class="fa-regular fa-copy"></i>
            </button>
        </div>
    </div>
    """

    return f"""
    {input_area}
    <div class="flex items-center justify-between bg-gray-50 p-3 rounded-lg border border-gray-100">
        <div class="flex items-center gap-3">
            {controls}
        </div>
    </div>
    {output_area}
    """

def get_tool_js(tool):
    logic_type = tool.get('logic_type')
    base_js = LOGIC_TEMPLATES.get(logic_type, '')
    
    if logic_type == 'camera':
        return """
        async function startCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                document.getElementById('video').srcObject = stream;
            } catch(e) {
                showToast('Camera access denied', 'error');
            }
        }
        function takePhoto() {
            const video = document.getElementById('video');
            const canvas = document.getElementById('canvas');
            const photo = document.getElementById('photo');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            photo.src = canvas.toDataURL('image/png');
            photo.classList.remove('hidden');
        }
        """

    return base_js

# ==========================================
# 4. Main Execution
# ==========================================

def main():
    for tool in TOOLS:
        # Generate English
        fname = tool['id'] + '.html'
        with open(fname, 'w') as f:
            f.write(get_html(tool, 'en'))
        print(f"Generated {fname}")
        
        # Generate Chinese
        fname_zh = tool['id'] + '-zh.html'
        with open(fname_zh, 'w') as f:
            f.write(get_html(tool, 'zh'))
        print(f"Generated {fname_zh}")

if __name__ == '__main__':
    main()
