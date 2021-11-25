class script(object):
    START_TXT = """Chibai le! {},
Kei hi <a href=https://t.me/{}>{}</a>, ka ni e!

<b>Fakna Track/Copy ka pe thei reng che a nia.</b>

Min hmandân túr kim chang i hriat duh chuan <a href=https://t.me/zaipawl/247>Hetah hmet la</a>, i hre thei mai ang."""

    HELP_TXT = """Hey! {},
<b>A hnuaia Modules ah hian ka puih theihna tur che a awm.</b>"""

    ABOUT_TXT = """<b>➥ My name: {}
➥ Creator: Zaute Km
➥ Library: Pyrogram
➥ Language: Python 𝟹
➥ Data Base: MongoDB
➥ Bot Server: AWS
➥ Build Status: v1.0.1 [ Beta ]

<a href='https://t.me/joinchat/prE6ALN6x2hkY2E1'>© Sᴇʀɪᴇs Sᴛᴜᴅɪᴏ Oғғɪᴄɪᴀʟ ™</a></b>"""

    SOURCE_TXT = """<b>NOTE:</b>
- Zaipawl Source Code Open a ni. 
- Source: <a href='https://github.com/ZauteKm/Zaipawl-Bot'>GitHub 👉 Click here</a>

<b>DEVS:</b>
- <a href=https://t.me/zautekm>Zaute Km</a>

<b>GROUPS:</b>
- <a href='https://t.me/joinchat/prE6ALN6x2hkY2E1'>ZoSeries Studio</a>
- <a href='https://t.me/mizotelegram'>Mizo Infotel Group</a>
- <a href='https://t.me/solfazirna'>Music (Sound) Zirna</a>
- <a href='https://t.me/joinchat/S1H92QODxvJiYWU1'>Zoram Hnaruak</a>

<b>CHANNELS:</b>
- <a href='https://t.me/mizotginfotel'>Mizo Infotel Channel</a>
- <a href='https://t.me/zaipawl'>Fakna Rimâwi Huang</a>
- <a href='https://t.me/chanchinbu'>Chanchin Bu</a>
- <a href='https://t.me/joinchat/KfaibJOuootkNWQ1'>Hnaruak Post-Na</a>"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Dingdi hi admin-ah dah phawt rawh.
2. Group Admin chauhin filter hi a siam thei.
3. Alert buttons limit hi 64 characters a ni.

<b>Commands leh Hmandân:</b>
• /filter - <code>Group-a filter siamna.</code>
• /filters - <code>Group-a filters Save zawng zawng.</code>
• /del - <code>Filter save pakhat chiah delete-na.</code>
• /delall - <code>Filter save zawng zawng delete-na. (Group Owner Chauh)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Dingdi hian both url leh alert inline buttons a Support.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Dingdi supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mizotelegram)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands leh Hmandân:</b>
• /connect  - <code>Private Chat-a Connect na.</code>
• /disconnect  - <code>Group Disconnect lehna.</code>
• /connections - <code>Connections zawng² enna.</code>"""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• Dingdi should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• Dingdi should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specifed user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• Dingdi should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• Dingdi should have admin privillage.
• These commands works on both pm and group.
• Dingdi can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• Dingdi should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
He Modules te hi Bot Owner chauhin a ti thei.

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 Groups aṭanga Movie i rawn Request kha, Hetah ka pek theihna tur che in ka Official Channel i join hmasak phawt a ngai. Chuan, Groups aṭanga i Movie rawn Request te hi Private ah ka pe zêl thei ang che 🙈__

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
