from config import URL_VPN

lexicon = {
    'ru': {
        'start_message': '''
Привет👋\n\n
FreeVPN — самый быстрый и полностью бесплатный VPN-сервис.

⚡️ Наивысшая скорость
💸 100% бесплатно
🔋 Аккумулятор не разряжается
💻 Работает на любых устройствах iOS, Android, Windows, MacOS, Android TV
Жми на кнопку 📌 «Подключиться» и получи доступ к VPN 👇
        ''',
        'change_connect': 'Выберите свое устройство ниже👇 для получения инструкции',
        'connect_faq': '''
1️⃣ Скачайте и установите приложение Happ нажав на первую кнопку ниже «🌐Скачать приложение»
2️⃣ Выполните пошаговый алгоритм подключения к VPN нажав на вторую кнопку ниже «🔑Выполнить подключение»
        ''',
        'connect_algoritm': f'''
1️⃣ Скопируйте ссылку для подключения ниже:
`{URL_VPN}` 
2️⃣ Нажмите на кнопку Clipboard для вставки скопированной ссылки из буфера
3️⃣ Нажмите на большую кнопку в приложении Happ и наслаждайтесь скоростью.
        ''',
        'ref': '''
👥 Не позволяй своим друзьям платить за ВПН 😇
📤 Жми на кнопку ниже и отправь им ссылку на наш бесплатный ВПН 👇
        ''',
        'offer': '📄 ℹ️Выберите необходимый пункт:',
        'help_main_text': 'Выберите ваш тип устройства ниже и получите список частых проблем и пути их решения 👇',
        'help_android_text': 'Выберите вопрос:',
        'windows_browser_issue': '''
Отключите все расширения в браузере.
Обычно мешают такие расширения: впн, прокси, обход рунета и тд.
''',

        'windows_telegram_issue': '''
В настройках прокси в Телеграм выставите галочку возле пункта «Системные настройки прокси».
''',

        'windows_internet_issue': '''
Для решения этой проблемы следуйте инструкции ниже 👇 

1️⃣ Зажмите клавиши Win + R
2️⃣ В открывшемся окне напишите inetcpl.cpl и нажмите на ENTER
3️⃣ Перейди на вкладку Подключения → Настройки сети и убедись, что "Использовать прокси-сервер" выключено
''',
        'invalid_key_text': '''
Если подобная ошибка появляется, нужно убедиться что не включен другой vpn. При первой установке когда появлялось диалоговое окно с просьбой добавить профиль ВПН, вы отказались.

Для решения этой проблемы следуйте инструкции ниже 👇

1️⃣ Удалите приложение Vlessoff и установите заново.
2️⃣ После установки согласитесь добавить профиль ВПН.
3️⃣ Вставьте ваш код с бота и подключайтесь.''',
        'slow_vpn_text': '''
Плохая работа ВПН чаще всего связанна с вашим интернет соединением, с нашей стороны сервера работают без перебоев.

Для решения этой проблемы вы можете попробовать решение ниже👇 

Зайдите в настройки телефона > Перенос или сброс > Сбросить > Сбросить настройки сети

Не переживайте, с телефона ничего не пропадет.
''',
        'auto_disconnect_text': '''
Зачастую эта проблема возникает если:
- Заполнена память
- Включен энергосберегающий режим 
- Плохое соединение с интернетом на телефоне
''',
        'tiktok_not_working_text': '''
Чтоб заработал новый Тикток на следуйте инструкции ниже 👇

1️⃣ Удаляем приложение Тикток

2️⃣ Включаем ВПН

3️⃣ Скачиваем тикток и наслаждаемся 😊
''',
        'mobile_network_text': '''
Проверьте в приложении вашего оператора ваш пакет интернета.
Зачастую это бывает когда трафик закончился, но остался пакет «Безлимит на соц сети».
В таком случае впн не будет работать, так как он не является соц сетью.
''',
        'cant_install_text': '''
Для установки последней версии приложения впн следуйте инструкции ниже 👇

1️⃣ Заходите в бот телеграм нашего впн

2️⃣ Напишите /start и откроется главное меню

2️⃣ Нажмите на кнопку 🔑Установить ВПН > Выберите тип устройства > Следуйте инструкции бота.

 Готово, можете подключаться ⚡️
 ''',
        'config_error_text': '''
Вы вставили вашу подписку в приложение, но не выбрали ее для подключения.

Вам нужно 👇

1️⃣ Нажать на вашу подписку в приложении v2raytun (Она загорится синим).
2️⃣ Нажать на большую кнопку и подключиться.
''',
        'friend_days_text': '''Дни за приглашенного друга не зачисляются только если друг уже состоял ранее в боте или перешел по неправильной ссылке.''',

        'buttons': {
            'connect': '📌 Подключиться бесплатно',
            'friends': '👥 Пригласить друзей',
            'help': '❓ Помощь',
            'offer': '📄 Оферта',
            'get_app': '🌐 Скачать приложение',
            'get_connect': '🔑 Выполнить подключение',
            'share': '📤 Поделиться',
            'politic': '🛡️ Политика конфиденциальности',
            'politic_back': '🔄 Политика возврата',
            'help_android': '📱 Android',
            'help_ios': '🍎 iOS',
            'help_windows': '🪟 Windows',
            'help_macos': '💻 macOS',
            'invalid_key': 'Неверный ключ в подключении',
            'slow_vpn': 'ВПН работает медленно',
            'auto_disconnect': 'ВПН сам по себе отключается',
            'tiktok_not_working': 'Не работает TikTok',
            'mobile_network': 'Не работает впн через мобильную сеть',
            'cant_install': 'Не могу установить ВПН',
            'config_error': 'Ошибка "Не выбрана конфигурация"',
            'friend_days': 'Не зачислились дни за приглашения друга',
            'back': '🔙 Назад',
            'main_menu': '🔙 Главное меню'
        }
    },
    'de': {
        'start_message': '''
Hallo 👋\n\n
FreeVPN ist der schnellste und vollständig kostenlose VPN‑Dienst.

⚡️ Höchste Geschwindigkeit
💸 100 % kostenlos
🔋 Entlädt den Akku nicht
💻 Funktioniert auf allen Geräten: iOS, Android, Windows, macOS, Android TV
Tippe auf die Schaltfläche 📌 „Verbinden“, um Zugriff auf das VPN zu erhalten 👇
        ''',
        'change_connect': 'Wähle unten dein Gerät 👇, um die Anleitung zu erhalten',
        'connect_faq': '''
1️⃣ Lade die App Happ herunter und installiere sie, indem du unten auf die erste Schaltfläche „🌐 App herunterladen“ tippst
2️⃣ Folge der Schritt‑für‑Schritt‑Anleitung, indem du unten auf die zweite Schaltfläche „🔑 Verbindung einrichten“ tippst
        ''',
        'connect_algoritm': f'''
1️⃣ Kopiere den Verbindungslink unten:
`{URL_VPN}` 
2️⃣ Tippe auf die Schaltfläche Clipboard, um den kopierten Link aus der Zwischenablage einzufügen
3️⃣ Tippe in der Happ‑App auf die große Taste und genieße die Geschwindigkeit.
        ''',
        'ref': '''
👥 Lass deine Freunde nicht für VPN bezahlen 😇
📤 Tippe unten auf die Schaltfläche und sende ihnen den Link zu unserem kostenlosen VPN 👇
        ''',
        'offer': '📄 ℹ️ Wähle den gewünschten Punkt:',
        'help_main_text': 'Wähle unten deinen Gerätetyp und erhalte eine Liste häufiger Probleme und deren Lösungen 👇',
        'help_android_text': 'Wähle eine Frage:',
        'windows_browser_issue': '''
Deaktiviere alle Erweiterungen im Browser.
Häufig stören solche Erweiterungen: VPN, Proxy, Runet‑Umgehung usw.
''',

        'windows_telegram_issue': '''
Setze in den Proxy‑Einstellungen von Telegram das Häkchen bei „System‑Proxy verwenden“.
''',

        'windows_internet_issue': '''
So löst du das Problem 👇 

1️⃣ Drücke Win + R
2️⃣ Gib im geöffneten Fenster inetcpl.cpl ein und drücke ENTER
3️⃣ Wechsle auf den Reiter Verbindungen → LAN‑Einstellungen und stelle sicher, dass „Proxyserver für LAN verwenden“ deaktiviert ist
''',
        'invalid_key_text': '''
Wenn ein solcher Fehler erscheint, stelle sicher, dass kein anderer VPN aktiv ist. Bei der ersten Installation hast du möglicherweise das Dialogfenster zum Hinzufügen eines VPN‑Profils abgelehnt.

So löst du das Problem 👇

1️⃣ Deinstalliere die App Vlessoff und installiere sie erneut.
2️⃣ Stimme nach der Installation zu, das VPN‑Profil hinzuzufügen.
3️⃣ Füge deinen Code aus dem Bot ein und verbinde dich.''',
        'slow_vpn_text': '''
Schlechte VPN‑Leistung liegt meist an deiner Internetverbindung; auf unserer Seite laufen die Server ohne Unterbrechungen.

Zur Lösung kannst du Folgendes ausprobieren 👇 

Öffne die Telefoneinstellungen > Übertragen oder Zurücksetzen > Zurücksetzen > Netzwerkeinstellungen zurücksetzen

Keine Sorge, deine Daten bleiben erhalten.
''',
        'auto_disconnect_text': '''
Dieses Problem tritt häufig auf, wenn:
- der Speicher voll ist
- der Energiesparmodus aktiviert ist 
- die Internetverbindung auf dem Telefon schlecht ist
''',
        'tiktok_not_working_text': '''
Damit der neue TikTok funktioniert, folge der Anleitung 👇

1️⃣ TikTok deinstallieren

2️⃣ VPN einschalten

3️⃣ TikTok herunterladen und genießen 😊
''',
        'mobile_network_text': '''
Prüfe in der App deines Mobilfunkanbieters dein Datenpaket.
Oft ist das Datenvolumen aufgebraucht, aber das Paket „Unbegrenzt für soziale Netzwerke“ ist noch aktiv.
In diesem Fall funktioniert das VPN nicht, da es keine soziale Plattform ist.
''',
        'cant_install_text': '''
Um die neueste Version der VPN‑App zu installieren, folge der Anleitung 👇

1️⃣ Öffne unseren VPN‑Telegram‑Bot

2️⃣ Sende /start – das Hauptmenü öffnet sich

2️⃣ Tippe auf 🔑 VPN installieren > Wähle den Gerätetyp > Folge der Bot‑Anleitung.

 Fertig, du kannst dich verbinden ⚡️
 ''',
        'config_error_text': '''
Du hast dein Abonnement in der App eingefügt, es aber nicht für die Verbindung ausgewählt.

Du musst 👇

1️⃣ In der App v2raytun auf dein Abonnement tippen (es wird blau markiert).
2️⃣ Auf die große Taste tippen und verbinden.
''',
        'friend_days_text': '''Tage für einen eingeladenen Freund werden nur dann nicht gutgeschrieben, wenn der Freund bereits zuvor im Bot war oder dem falschen Link gefolgt ist.''',

        'buttons': {
            'connect': '📌 Kostenlos verbinden',
            'friends': '👥 Freunde einladen',
            'help': '❓ Hilfe',
            'offer': '📄 Angebot',
            'get_app': '🌐 App herunterladen',
            'get_connect': '🔑 Verbindung einrichten',
            'share': '📤 Teilen',
            'politic': '🛡️ Datenschutzerklärung',
            'politic_back': '🔄 Rückerstattungsrichtlinie',
            'help_android': '📱 Android',
            'help_ios': '🍎 iOS',
            'help_windows': '🪟 Windows',
            'help_macos': '💻 macOS',
            'invalid_key': 'Ungültiger Verbindungsschlüssel',
            'slow_vpn': 'VPN ist langsam',
            'auto_disconnect': 'VPN trennt sich von selbst',
            'tiktok_not_working': 'TikTok funktioniert nicht',
            'mobile_network': 'VPN funktioniert im Mobilfunknetz nicht',
            'cant_install': 'VPN lässt sich nicht installieren',
            'config_error': 'Fehler „Keine Konfiguration ausgewählt“',
            'friend_days': 'Tage für eingeladenen Freund wurden nicht gutgeschrieben',
            'back': '🔙 Zurück',
            'main_menu': '🔙 Hauptmenü'
        }
    }
}
