import os, json, random
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, ))
TEMPLATE_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "bin", "db", "templates"))

ICONS = ["🙂","😀","😄","😆","😅","😂","🤣","😊","☺️","😌","😉","😏","😍","😘","😗","😙","😚","🤗","😳","🙃","😇","😈","😛","😝","😜","😋","🤤","🤓","😎","🤑","😒","🙁","☹️","😞","😔","😖","😓","😢","😭","😟","😣","😩","😫","😕","🤔","🙄","😤","😠","😡","😶","🤐","😐","😑","😯","😲","😧","😨","😰","😱","😪","😴","😬","🤥","🤧","🤒","😷","🤕","😵","🤢","🤠","🤡","👿","👹","👺","👻","💀","👽","👾","🤖","💩","🎃","👍","👎","✌️","🤞","👌","🤙","🤘","🖕","☝️","💅","👉","👈","👇","👆","👊","✊","🤜","🤛","💪","✍️","🙏","🤳","👏","🤝","🙌","👐","✋","🖐️","👋","🖖","👂","👃","👁️","👀","👁️‍🗨️","👅","👣","👤","👥","🗣️","👶","👦","👧","👨","👩","👱","👴","👵","🎅","🤶","👮","👷","💂","🕵️","👳","👲","🤵","👰","🤴","👸","🙋","💁","🙅","🙆","🤷","🤦","🙎","🙍","💆","💇","🤰","👯","🙇","👼","💑","👩‍❤️‍👩","👨‍❤️‍👨","💏","👩‍❤️‍💋‍👩","👨‍❤️‍💋‍👨","🚶","🏃","🕴️","💃","🕺","🛀","🛌","👫","👭","👬","🤸","🏋️","⛹️","🤾","⛷️","🏂","🏌️","🏄","🏊","🤽","🤺","🤼","🚣","🏇","🚴","👪","👨‍👩‍👧","👨‍👩‍👧‍👦","👨‍👩‍👦‍👦","👨‍👩‍👧‍👧","👩‍👩‍👦","👩‍👩‍👧","👩‍👩‍👧‍👦","👩‍👩‍👦‍👦","👩‍👩‍👧‍👧","👨‍👨‍👦","👨‍👨‍👧","👨‍👨‍👧‍👦","👨‍👨‍👦‍👦","👨‍👨‍👧‍👧","♥️","❤️","💛","💚","💙","💜","🖤","💖","💝","💔","❣️","💕","💞","💓","💗","💘","💟","💌","💋","👄","💄","💍","📿","🎁","👙","👗","👚","👕","👘","🎽","👘","👖","👠","👡","👢","👟","👞","👒","🎩","🎓","👑","⛑️","👓","🕶️","🌂","👛","👝","👜","💼","🎒","🛍️","🛒","🎭","🎦","🎨","🤹","🎊","🎉","🎈","🎧","🎷","🎺","🎸","🎻","🥁","🎹","🎤","🎵","🎶","🎼","⚽","🏀","🏈","⚾","🏐","🏉","🎱","🎾","🏸","🏓","🏏","🏑","🏒","🥅","⛸️","🎿","🥊","🥋","⛳","🎳","🏹","🎣","🎯","🚵","🎖️","🏅","🥇","🥈","🥉","🏆","🍏","🍎","🍐","🍊","🍋","🍌","🍉","🍇","🍓","🍈","🥝","🥑","🍍","🍒","🍑","🍆","🥒","🥕","🌶","🌽","🍅","🥔","🍠","🌰","🥜","🍯","🥐","🍞","🥖","🧀","🥚","🍳","🥓","🍤","🍗","🍖","🍕","🌭","🍔","🍟","🥙","🌮","🌯","🥗","🥘","🍝","🍜","🍲","🍣","🍱","🍛","🍚","🍙","🍘","🍢","🍡","🍧","🍨","🍦","🥞","🍰","🎂","🍮","🍭","🍥","🍬","🍫","🍿","🍩","🍪","🍼","🥛","☕","🍵","🍶","🍺","🍻","🥂","🍷","🥃","🍸","🍹","🍾","🥄","🍴","🍽","😺","😸","😹","😻","😼","😽","🙀","😿","😾","🐱","🐶","🐰","🐭","🐹","🦊","🐻","🐼","🐨","🐯","🦁","🐮","🐗","🐷","🐽","🐸","🐵","🙈","🙉","🙊","🦍","🐺","🐑","🐐","🐏","🐴","🦄","🦌","🦏","🦅","🐤","🐣","🐥","🐔","🐓","🦃","🐦","🦆","🦇","🦉","🕊️","🐧","🐕","🐩","🐈","🐇","🐁","🐀","🐿","🐒","🐖","🐆","🐅","🐃","🐂","🐄","🐎","🐪","🐫","🐘","🐊","🐢","🐠","🐟","🐡","🐬","🦈","🐳","🐋","🦑","🐙","🦐","🐚","🦀","🦂","🦎","🐍","🐛","🐜","🕷️","🕸️","🐞","🦋","🐝","🐌","🐲","🐉","🐾","🌼","🌸","🌺","🏵️","🌻","🌷","🌹","🥀","💐","🌾","🎋","☘","🍀","🍃","🍂","🍁","🌱","🌿","🎍","🌵","🌴","🌳","🎄","🍄","🌎","🌍","🌏","🌜","🌛","🌕","🌖","🌗","🌘","🌑","🌒","🌓","🌔","🌚","🌝","🌙","💫","⭐","🌟","✨","⚡","🔥","💥","☄️","🌞","☀️","🌤️","⛅","🌥️","🌦️","☁️","🌧️","⛈️","🌩️","🌨️","🌈","💧","💦","☂️","☔","🌊","🌫","🌪","💨","❄","🌬","⛄","☃️","🚗","🚕","🚙","🚌","🚎","🏎","🚓","🚑","🚒","🚐","🚚","🚛","🚜","🛴","🚲","🛵","🏍","🚘","🚖","🚍","🚔","🚨","💺","✈","🛫","🛬","🛩","🚁","🚀","🛰","🚡","🚠","🚟","🚃","🚋","🚞","🚝","🚄","🚅","🚈","🚂","🚆","🚊","🚇","🚉","🛶","⛵","🛥","🚤","🚢","⛴","🛳","⚓","🚧","⛽","🚏","🚦","🚥","🛣","🛤","🏗","🏭","🏠","🏡","🏘","🏚","🏢","🏬","🏤","🏣","🏥","🏦","🏪","🏫","🏨","🏩","🏛","🏰","🏯","🏟️","⛪","💒","🕌","🕍","🕋","⛩","🗼","🗿","🗽","🗺","🎪","🎠","🎡","🎢","⛲","⛱","🏖","🏝","🏕","⛺","🗾","⛰","🏔","🗻","🌋","🏞","🏜","🌅","🌄","🎑","🌠","🎇","🎆","🏙","🌇","🌆","🌃","🌌","🌉","🌁","📱","📲","💻","🖥","⌨","🖨","🖱","🖲","🕹","🎮","💽","💾","💿","📀","📼","📷","📸","📹","🎥","📽","🎞","🎬","📞","☎","📟","📠","📺","📻","🎙","🎚","🎛","📡","📢","📣","🔔","💡","🕯","🔦","🔋","🔌","⌚","⏱","⏲","⏰","🕰","⌛","⏳","🔮","💎","🎲","🎰","💸","💵","💴","💶","💷","💰","💳","💲","💱","⚖","🔫","💣","🔪","🗡","⚔","🛡","🚬","⚰","⚱","🗜️","🔧","🔨","⚒","🛠","⛏","🔩","⚙","⛓","💈","🌡","💊","💉","⚗","🔬","🔭","🚿","🛁","🚽","🛎","🔑","🗝","🚪","🛋","🛏","🖼","🏺","🗑","🛢","🕳","🏮","🎏","🎎","🎐","🎫","🎟️","🎀","🎗️","📯","✉","📩","📨","📧","📦","📪","📫","📬","📭","📮","📥","📤","📜","📃","📄","📑","📊","📈","📉","🗒","📅","📆","🗓","📇","🗃","🗳","🗄","📋","📁","📂","🗂","📓","📔","📒","📕","📗","📘","📙","📚","📖","🗞","📰","📝","✏","🖊","🖍","🖌","🖋","✒","📌","📍","📎","🖇","🔖","🏷","🔗","🔍","🔎","📐","📏","✂","🔒","🔓","🔏","🔐","❗","❕","❓","❔","‼️","⁉️","✅","❌","⭕","💢","🚫","🔞","📵","🔇","🔕","🚭","🚳","🚱","🚷","🚯","🛑","⛔","🚸","⚠️","☢️","☣️","☠️","❎","♻️","☯️","💯","💤","🔆","🔅","🌀","♨️","✴️","✳️","🌐","🔈","🕎","⚜️","🔱","〽️","〰️","🔚","🔙","🔛","🔝","🔜","✡️","✝️","☦️","☪️","🕉️","☸️","🛐","☮️","⚛️","❇️","♀️","♂️","✔️","✖️","➕","➖","➗","©️","®️","™️","☑️","🚰","🛄","🛅","🛂","🛃","Ⓜ️","🅿️","🚾","🏧","🚮","♿","🚹","🚺","🚻","🚼","🆚","📴","📳","🆘","🆗","🆙","🆒","🆖","🆕","🆓","🔠","🔤","🔡","🔣","🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹","🇺","🇻","🇼","🇾","🇽","🇿","0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟","🔢","#️⃣","*️⃣","ℹ️","📶","▶️","⏸️","⏹️","⏺️","⏯️","◀️","🔼","🔽","⏩","⏪","⏫","⏬","⏮️","⏭️","⏏️","🔀","🔁","🔂","🔄","🔃","↩️","↪️","⤴️","⤵️","⬆️","⬇","⬅️","➡️","↗️","↙️","↘️","↖️","↔️","↕️","♈","♉","♊","♋","♌","♍","♎","♏","♐","♑","♒","♓","⛎","🆔","🈳","🈂️","🈁","🈯","🈹","🈚","🈶","🈷️","🈸","🈺","🉑","㊗️","㊙️","🈴","🈲","🅰️","🅱️","🆎","🅾️","🆑","🔰","📛","💮","💠","🔶","🔷","🔸","🔹","🔺","🔻","▪️","▫️","◾","◽","◼️","◻️","⬛","⬜","🔲","🔳","⚪","⚫","🔴","🔵","🔘","🗨️","💭","🗯️","💬","➰","♠️","♣️","♦️","🃏","🀄","🎴","💹","🔉","🔊","➿","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚","🕛","🕧","🕜","🕝","🕞","🕟","🕠","🕡","🕢","🕣","🕤","🕥","🕦","🏳️","🏴","🏁","🚩","🏳️‍🌈","🇦🇫","🇦🇽","🇦🇱","🇩🇿","🇦🇸","🇦🇩","🇦🇴","🇦🇮","🇦🇶","🇦🇬","🇦🇷","🇦🇲","🇦🇼","🇦🇺","🇦🇹","🇦🇿","🇧🇸","🇧🇭","🇧🇩","🇧🇧","🇧🇾","🇧🇪","🇧🇿","🇧🇯","🇧🇲","🇧🇹","🇧🇴","🇧🇶","🇧🇦","🇧🇼","🇧🇷","🇮🇴","🇻🇬","🇧🇳","🇧🇬","🇧🇫","🇧🇮","🇨🇻","🇰🇭","🇨🇲","🇨🇦","🇮🇨","🇰🇾","🇨🇫","🇹🇩","🇨🇱","🇨🇳","🇨🇽","🇨🇨","🇨🇴","🇰🇲","🇨🇬","🇨🇩","🇨🇰","🇨🇷","🇨🇮","🇭🇷","🇨🇺","🇨🇼","🇨🇾","🇨🇿","🇩🇰","🇩🇯","🇩🇲","🇩🇴","🇪🇨","🇪🇬","🇸🇻","🇬🇶","🇪🇷","🇪🇪","🇪🇹","🇪🇺","🇫🇰","🇫🇴","🇫🇯","🇫🇮","🇫🇷","🇬🇫","🇵🇫","🇹🇫","🇬🇦","🇬🇲","🇬🇪","🇩🇪","🇬🇭","🇬🇮","🇬🇷","🇬🇱","🇬🇩","🇬🇵","🇬🇺","🇬🇹","🇬🇬","🇬🇳","🇬🇼","🇬🇾","🇭🇹","🇭🇳","🇭🇰","🇭🇺","🇮🇸","🇮🇳","🇮🇩","🇮🇷","🇮🇶","🇮🇪","🇮🇲","🇮🇱","🇮🇹","🇯🇲","🇯🇵","🎌","🇯🇪","🇯🇴","🇰🇿","🇰🇪","🇰🇮","🇽🇰","🇰🇼","🇰🇬","🇱🇦","🇱🇻","🇱🇧","🇱🇸","🇱🇷","🇱🇾","🇱🇮","🇱🇹","🇱🇺","🇲🇴","🇲🇰","🇲🇬","🇲🇼","🇲🇾","🇲🇻","🇲🇱","🇲🇹","🇲🇭","🇲🇶","🇲🇷","🇲🇺","🇾🇹","🇲🇽","🇫🇲","🇲🇩","🇲🇨","🇲🇳","🇲🇪","🇲🇸","🇲🇦","🇲🇿","🇲🇲","🇳🇦","🇳🇷","🇳🇵","🇳🇱","🇳🇨","🇳🇿","🇳🇮","🇳🇪","🇳🇬","🇳🇺","🇳🇫","🇲🇵","🇰🇵","🇳🇴","🇴🇲","🇵🇰","🇵🇼","🇵🇸","🇵🇦","🇵🇬","🇵🇾","🇵🇪","🇵🇭","🇵🇳","🇵🇱","🇵🇹","🇵🇷","🇶🇦","🇷🇪","🇷🇴","🇷🇺","🇷🇼","🇧🇱","🇸🇭","🇰🇳","🇱🇨","🇵🇲","🇻🇨","🇼🇸","🇸🇲","🇸🇹","🇸🇦","🇸🇳","🇷🇸","🇸🇨","🇸🇱","🇸🇬","🇸🇽","🇸🇰","🇸🇮","🇸🇧","🇸🇴","🇿🇦","🇬🇸","🇰🇷","🇸🇸","🇪🇸","🇱🇰","🇸🇩","🇸🇷","🇸🇿","🇸🇪","🇨🇭","🇸🇾","🇹🇼","🇹🇯","🇹🇿","🇹🇭","🇹🇱","🇹🇬","🇹🇰","🇹🇴","🇹🇹","🇹🇳","🇹🇷","🇹🇲","🇹🇨","🇹🇻","🇺🇬","🇺🇦","🇦🇪","🇬🇧","🇺🇸","🇻🇮","🇺🇾","🇺🇿","🇻🇺","🇻🇦","🇻🇪","🇻🇳","🇼🇫","🇪🇭","🇾🇪","🇿🇲","🇿🇼",]
class TemplateHandler():
    @staticmethod
    def _read_template(option):
        _ = os.path.abspath(os.path.join(TEMPLATE_DIR, f"{option}.json"))
        if not os.path.exists(_): raise CustomError( f"{_} is not existed")
        with open(_) as f:
            return json.load(f)
    
    @staticmethod
    def get_template(payload):
        if "options" not in payload.keys(): raise CustomError( "'option' not in payload.keys()")
        else: template_obj = TemplateHandler._read_template(payload["options"])
        if "action" not in payload.keys(): raise CustomError( "'action' not in payload.keys()")
        else: _action = payload["action"] # defaul | random
        
        if _action not in template_obj.keys(): raise CustomError( "'action' not in template_obj.keys()")
        else: templates = template_obj[_action]

        title_templates = templates["title"]
        description_templates = templates["description"]

        title = title_templates[random.randint(0, len(title_templates) - 1)]
        description = description_templates[random.randint(0, len(description_templates) - 1)]
        
        return {
            "title": title,
            "description": description
        }
    
    @staticmethod
    def render_content(payload):
        if "product_info" not in payload.keys(): raise CustomError( "'product_info' not in payload.keys()")
        else: product_info = payload["product_info"]
        if "action" not in payload.keys(): raise CustomError( "'action' not in payload.keys()")
        else: action = payload["action"]
        print(product_info)
        if "options" not in product_info.keys(): raise CustomError( "'option' not in payload.keys()")
        if product_info["options"] == "real-estate":
            template = TemplateHandler.get_template({ "options": product_info["options"], "action": action })
            new_product_info = {}
            for key in product_info.keys():
                new_product_info[key] = product_info[key]
                if key == "id": new_product_info[key] = new_product_info[key].upper()
                if key == "district":
                    if product_info[key] == "dalat": new_product_info[key] = "TP. Đà Lạt"
                if key == "provide":
                    if product_info[key] == "lamdong": new_product_info[key] = "Tỉnh Lâm Đồng"
                if key == "ward":
                    if product_info[key] ==  "ward_1": new_product_info[key] = "Phường 1"
                    elif product_info[key] ==  "ward_2": new_product_info[key] = "Phường 2"
                    elif product_info[key] ==  "ward_3": new_product_info[key] = "Phường 3"
                    elif product_info[key] ==  "ward_4": new_product_info[key] = "Phường 4"
                    elif product_info[key] ==  "ward_5": new_product_info[key] = "Phường 5"
                    elif product_info[key] ==  "ward_6": new_product_info[key] = "Phường 6"
                    elif product_info[key] ==  "ward_7": new_product_info[key] = "Phường 7"
                    elif product_info[key] ==  "ward_8": new_product_info[key] = "Phường 8"
                    elif product_info[key] ==  "ward_9": new_product_info[key] = "Phường 9"
                    elif product_info[key] ==  "ward_10": new_product_info[key] = "Phường 10"
                    elif product_info[key] ==  "ward_11": new_product_info[key] = "Phường 11"
                    elif product_info[key] ==  "ward_12": new_product_info[key] = "Phường 12"
                    elif product_info[key] ==  "ward_tanung": new_product_info[key] = "Xã tanung"
                    elif product_info[key] ==  "ward_tramhanh": new_product_info[key] = "Xã tramhanh"
                    elif product_info[key] ==  "ward_xuantruong": new_product_info[key] = "Xã xuantruong"
                    elif product_info[key] ==  "ward_xuantho": new_product_info[key] = "Xã xuantho"
                if key == "street": new_product_info[key] = new_product_info[key].title()
                if key == "type":
                    if product_info[key] == "sell": new_product_info[key] = "bán"
                    elif product_info[key] == "rent": new_product_info[key] = "cho thuê"
                    elif product_info[key] == "assignment": new_product_info[key] = "sang nhượng"
                if key == "categories":
                    if product_info[key] == "house": new_product_info[key] = "nhà"
                    elif product_info[key] == "shophouse": new_product_info[key] = "nhà mặt tiền"
                    elif product_info[key] == "villa": new_product_info[key] = "villa (biệt thự)"
                    elif product_info[key] == "apartment": new_product_info[key] = "căn hộ/chung cư"
                    elif product_info[key] == "land": new_product_info[key] = "đất"
                    elif product_info[key] == "homestay": new_product_info[key] = "homestay"
                    elif product_info[key] == "hotel": new_product_info[key] = "khách sạn"
                    elif product_info[key] == "retailspace": new_product_info[key] = "mặt bằng kinh doanh"
                    elif product_info[key] == "workshop": new_product_info[key] = "kho/xưởng"
                    elif product_info[key] == "coffeehouse": new_product_info[key] = "quán coffee"
                if key == "building_line":
                    if product_info[key] == "motorbike": new_product_info[key] = "đường xe máy"
                    elif product_info[key] == "car": new_product_info[key] = "đường xe hơi"
                if key == "area": new_product_info[key] = str(product_info[key]) + "m2"
                if key == "furniture":
                    if product_info[key] == "none": new_product_info[key] = "không"
                    elif product_info[key] == "basic": new_product_info[key] = "cơ bản"
                    elif product_info[key] == "full": new_product_info[key] = "đầy đủ"
                if key == "legal":
                    if product_info[key] == "none": new_product_info[key] = "Không sổ"
                    elif product_info[key] == "snnc": new_product_info[key] = "Sổ nông nghiệp chung"
                    elif product_info[key] == "snnpq": new_product_info[key] = "Sổ nông nghiệp phân quyền"
                    elif product_info[key] == "srnn": new_product_info[key] = "Sổ nông nghiệp riêng"
                    elif product_info[key] == "sxdc": new_product_info[key] = "Sổ xây dựng chung"
                    elif product_info[key] == "sxdpq": new_product_info[key] = "Sổ xây dựng phân quyền"
                    elif product_info[key] == "srxd": new_product_info[key] = "Sổ xây dựng riêng"
                if key == "price":
                    if product_info["type"] == "sell": new_product_info[key] = str(product_info[key]) + "tỷ"
                    elif product_info["type"] == "rent": new_product_info[key] = str(product_info[key]) + "triệu/tháng"
                    elif product_info["type"] == "assignment": new_product_info[key] = str(product_info[key]) + "triệu/tháng"

            template["description"] = template["description"].split("\n")
            for index, des in enumerate(template["description"]):            
                if product_info["type"] == "rent" or product_info["type"] == "assignment":
                    if "{legal}" in des:template["description"].pop(index)
                    if "{area}" in des:template["description"].pop(index)
                if product_info["categories"] in ["apartment", "land", "retailspace", "workshop", ]:
                    if "{construction}" in des: template["description"].pop(index)
            template["description"] = "\n".join(template["description"])

            for key in new_product_info.keys():
                if f"{{{key}}}" in template["title"]:
                    template["title"] = template["title"].replace(f"{{{key}}}", str(new_product_info[key]))
                    prev_title = template["title"]
                    while prev_title != template["title"].replace("{icon}", ICONS[random.randint(0, len(ICONS) - 1)], 1):
                        prev_title = template["title"]
                        template["title"] = template["title"].replace("{icon}", ICONS[random.randint(0, len(ICONS) - 1)], 1)
                if f"{{{key}}}" in template["description"]:
                    template["description"] = template["description"].replace(f"{{{key}}}", str(new_product_info[key]))
                    prev_description = template["description"]
                    while prev_description != template["description"].replace("{icon}", ICONS[random.randint(0, len(ICONS) - 1)], 1):
                        prev_description = template["description"]
                        template["description"] = template["description"].replace("{icon}", ICONS[random.randint(0, len(ICONS) - 1)], 1)
            
            template["title"] = template["title"].upper()
            return template
        elif product_info["options"] == "miscellaneous": CustomError("invalid option")
        else: raise("invalid option")
class CustomError(Exception):
    pass

if __name__ == "__main__":
    TemplateHandler.render_content({
        "action": "default",
        "product_info": {
                "options": "real-estate",
                "images": [
                    "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244/re.s.100924.5244_0.png",
                    "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244/re.s.100924.5244_1.png",
                    "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244/re.s.100924.5244_2.png",
                    "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244/re.s.100924.5244_3.png",
                    "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244/re.s.100924.5244_4.png",
                    "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.s.100924.5244/re.s.100924.5244_5.png"
                ],
                "id": "re.s.100924.123",
                "provide": "l\u00e2m \u0111\u1ed3ng",
                "district": "\u0111\u00e0 l\u1ea1t",
                "ward": "ward_11",
                "street": "ph\u1ea1m h\u1ed3ng th\u00e1i",
                "type": "sell",
                "categories": "house",
                "building_line": "car",
                "area": 87.75,
                "construction": "1 h\u1ea7m, 1 tr\u1ec7t, 3 l\u1ea7u",
                "function": "1pk, 1 b\u1ebfp, 5pn, 6wc",
                "furniture": "full",
                "legal": "srxd",
                "price": 14.5,
                "description": "'\n+ nh\u00e0 m\u1edbi, s\u1ea1ch s\u1ebd, g\u1ecdn g\u00e0ng, c\u00f3 h\u1ed3 b\u01a1i\n+ ngang 4.5m\n+ kqh b\u00e0i b\u1ea3n, \u0111\u01b0\u1eddng xe h\u01a1i r\u1ed9ng r\u00e3i\n+ t\u1eb7ng to\u00e0n b\u1ed9 \u0111\u00e1 phong thu\u1ef7 cho ch\u1ee7 m\u1edbi \u1ea1; khu v\u1ef1c y\u00ean t\u0129nh th\u00edch h\u1ee3p ngh\u1ec9 d\u01b0\u1ee1ng"
            }
    })

