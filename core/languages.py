MESSAGES = {
    "az": {
        "daily_chess_images": "📷 Günün şahmat şəkilləri burada! Divar kağızı kimi istifadə et və ya dostlarınla paylaş! 🏆♟️",
        "puzzle_message": (
            "♟️ **Günün Şahmat Tapmacası**\n\n"
            "🔗 [Tapmacanı burada həll et]({url})\n"
            "📊 Çətinlik: {rating} Elo\n"
            "👀 Oynanılıb: {plays} dəfə"
        ),
        "puzzle_error": "⚠️ Gündəlik tapmaca əldə edilə bilmədi. Zəhmət olmasa, sonra yenidən yoxlayın.",
        "set_rating_usage": (
            "⚠️ Zəhmət olmasa Chess.com və ya Lichess.org istifadəçi adını daxil edin.\n\n"
            "✅ Doğru istifadə:\n"
            "`/setrating StrongJunior`"
        ),
        "topplayers_header": "🏆 **Ən Yüksək Reytinqə Sahib Oyunçular**",
        "topplayers_no_data": "⚠️ Hələ heç bir istifadəçi reytinq təyin etməyib.",
        "set_rating_not_found": "❌ `{username}` adlı istifadəçi tapılmadı və ya reytinqi yoxdur.",
        "set_rating_success": "✅ `{username}` üçün reytinq uğurla təyin edildi: `{rating}`.",
        "no_top_players": "⚠️ Hələ heç bir istifadəçi reytinqini təyin etməyib.",
        "top_players_header": "🏆 **Ən Yüksək Reytinqli Oyunçular:**",
        "rating_user_not_found": "❌ Bu istifadəçi Chess.com və ya Lichess.org saytında tapılmadı.",
        "rating_not_found": "⚠️ Bu istifadəçinin reytinqi tapılmadı.",
        "rating_set_success": "✅ Reytinqiniz uğurla təyin edildi: `{rating}`",
        "lichess_profile_usage": "⚠️ İstifadəçi adını qeyd et. Məs: `/lichessprofile StrongJunior`",
        "lichess_profile_not_found": "❌ `{}` adlı istifadəçi tapılmadı.",
        "lichess_profile_header": "📊 **Lichess.org Profil Məlumatı**: `{}`\n\n",
        "chess_profile_usage": "⚠️ İstifadəçi adını qeyd et. Məs: `/chessprofile shakhriyar-mamedyarov`",
        "chess_profile_not_found": "❌ `{}` adlı istifadəçi tapılmadı.",
        "chess_profile_header": "📊 **Chess.com Profil Məlumatı**: `{}`\n\n",
        "rating_bullet": "♞ **Bullet Rating**: {}",
        "rating_blitz": "♞ **Blitz Rating**: {}",
        "rating_rapid": "♞ **Rapid Rating**: {}",
        "rating_daily": "♞ **Daily Rating**: {}",
        "total_games": "📌 **Ümumi oyunlar**: {}",
        "games_won": "🔥 **Qazandığı oyunlar**: {} ({}%)",
        "games_lost": "❌ **Uduzduğu oyunlar**: {}",
        "games_drawn": "🤝🏻 **Bərabərə qaldığı oyunlar**: {}",
        "view_profile": "👀 **Profilə bax**: [Buraya kliklə]({})",
        "donate_message": (
            "☕ **Bot olsam da qəhvəni sevirəm!😒 **\n\n"
            "Əgər məni bəyəndin və dəstək olmaq istəyirsənsə, "
            "məni kiçik bir qəhvə ilə sevindirə bilərsən. 😌\n\n"
            "👉 [Buradan dəstək ol!](https://buymeacoffee.com/thehormat)"
        ),
        "unsubscribe_success": "❌ Bildirişlərdən çıxarıldın. Artıq şahmat faktları almayacaqsan. Kasparovun gözünə görünmə...",
        "unsubscribe_already": "⚠️ Sən artıq bildirişlərdən çıxmısan!",
        "start_welcome": "✅ Aramıza xoş gəldin dostum! Hər gün şahmat haqqında maraqlı və öyrədici məlumatlar alacaqsan. Tal səninlə fəxr edir ♟️",
        "start_already_registered": "🔹 Sən artıq qeydiyyatdan keçmisən! Bu istəyini tüm şahmat sevərlər bəyəndi. ♟️",
        "lichess_arena_header": "🏆 **Lichess.org Aktif Turnirlər:**\n\n",
        "lichess_arena_no_tournaments": "❌ Bu rating üçün uyğun turnir tapılmadı.",
        "lichess_arena_starts_in": "(Başlamasına {} dəq qalıb)",
        "lichess_arena_error": (
            "⚠️ **Xəta!** Rating rəqəmlə olmalıdır.\n\n"
            "✅ Doğru istifadə:\n"
            "`/lichessarena 1500` (1500 rating üçün turnirləri göstərir)\n"
            "`/lichessarena` (Bütün açıq turnirləri göstərir)"
        ),
        "lichess_arena_no_data": "⚠️ Lichess.org arena datası alına bilmədi.",
        "language_set": "✅ Dil Azərbaycan dili olaraq təyin edildi!",
        "about": (
            "👋 *Salam!* Mən `ChessCast` botuyam, sənin şəxsi şahmat köməkçin. ♟️\n\n"
            "Mən sənə *gündəlik şahmat faktları*, *tapmacalar*, *real vaxtda turnir yeniləmələri* və "
            "*şahmatla bağlı maraqlı şəkillər* təqdim edirəm. "
            "**Lichess.org** və **Chess.com** üzərindən oyunçu profillərini və reytinqlərini yoxlaya bilərsən! 🎯\n\n"
            "📌 *Mən nə edə bilərəm?*\n\n"
            "♟️ *Gündəlik Şahmat Faktları:*\n"
            "/start - Botu aktiv et və ilk şahmat faktını al\n\n"
            "♟️ *Turnirlər & Oyunçular:*\n"
            "/lichessprofile `<istifadəçi_adı>` - Lichess.org oyunçu profilini gör\n"
            "/lichessarena `<istifadəçi_reytinqi>` - Lichess.org-da  açıq turnirləri gör\n"
            "/chessprofile `<istifadəçi_adı>` - Chess.com oyunçu profilini gör\n\n"
            "♟️ *Bildirişlər & İdarəetmə:*\n"
            "/unsubscribe - Bildirişləri dayandır və abunəliyi ləğv et\n"
            "/about - Bot haqqında məlumat al\n"
            "/language - Botun dilini dəyiş\n\n"
            " *Rəsmi telegram kanalımız 👇🏻*\n"
            "🔗 [Bütün yeniliklər üçün](https://t.me/chesscast)\n\n"
            " *Mənimlə şahmat oynamaq istəyirsən?*\n"
            "🤝🏻 [Profilim](https://lichess.org/@/StrongJunior)\n\n"
        ),
    },
    "en": {
        "daily_chess_images": "📷 Chess pictures of the day are here! Use as wallpaper or share with your friends! 🏆♟️",
        "puzzle_message": (
            "♟️ **Daily Chess Puzzle**\n\n"
            "🔗 [Solve the puzzle here]({url})\n"
            "📊 Difficulty: {rating} Elo\n"
            "👀 Played: {plays} times"
        ),
        "puzzle_error": "⚠️ Could not retrieve the daily puzzle. Please try again later.",
        "set_rating_usage": (
            "⚠️ Please enter your Chess.com or Lichess.org username.\n\n"
            "✅ Correct usage:\n"
            "`/setrating StrongJunior`"
        ),
        "topplayers_header": "🏆 **Top Rated Chess Players**",
        "topplayers_no_data": "⚠️ No users have set their rating yet.",
        "set_rating_not_found": "❌ User `{username}` not found or no rating available.",
        "set_rating_success": "✅ Rating for `{username}` has been successfully set: `{rating}`.",
        "no_top_players": "⚠️ No users have set their ratings yet.",
        "top_players_header": "🏆 **Top Rated Players:**",
        "rating_user_not_found": "❌ This user was not found on Chess.com or Lichess.org.",
        "rating_not_found": "⚠️ This user's rating was not found.",
        "rating_set_success": "✅ Your rating was successfully set: `{rating}`",
        "lichess_profile_usage": "⚠️ Enter a username. Example: `/lichessprofile StrongJunior`",
        "lichess_profile_not_found": "❌ User `{}` not found.",
        "lichess_profile_header": "📊 **Lichess.org Profile Information**: `{}`\n\n",
        "chess_profile_usage": "⚠️ Enter a username. Example: `/chessprofile shakhriyar-mamedyarov`",
        "chess_profile_not_found": "❌ User `{}` not found.",
        "chess_profile_header": "📊 **Chess.com Profile Information**: `{}`\n\n",
        "rating_bullet": "♞ **Bullet Rating**: {}",
        "rating_blitz": "♞ **Blitz Rating**: {}",
        "rating_rapid": "♞ **Rapid Rating**: {}",
        "rating_daily": "♞ **Daily Rating**: {}",
        "total_games": "📌 **Total games**: {}",
        "games_won": "🔥 **Games won**: {} ({}%)",
        "games_lost": "❌ **Games lost**: {}",
        "games_drawn": "🤝🏻 **Games drawn**: {}",
        "view_profile": "👀 **View profile**: [Click here]({})",
        "donate_message": (
            "☕ **Even as a bot, I love coffee!😒 **\n\n"
            "If you like me and want to support my work, "
            "you can treat me to a little coffee. 😌\n\n"
            "👉 [Support me here!](https://buymeacoffee.com/thehormat)"
        ),
        "unsubscribe_success": "❌ You have unsubscribed. You will no longer receive chess facts. Don't show up in Kasparov's sight...",
        "unsubscribe_already": "⚠️ You are already unsubscribed!",
        "start_welcome": "✅ Welcome, my friend! You will receive interesting and educational chess facts every day. Tal would be proud of you! ♟️",
        "start_already_registered": "🔹 You are already registered! Chess lovers appreciate your passion. ♟️",
        "lichess_arena_header": "🏆 **Lichess.org Active Tournaments:**\n\n",
        "lichess_arena_no_tournaments": "❌ No tournaments found for this rating.",
        "lichess_arena_starts_in": "(Starts in {} min)",
        "lichess_arena_error": (
            "⚠️ **Error!** Rating must be a number.\n\n"
            "✅ Correct usage:\n"
            "`/lichessarena 1500` (Shows tournaments for 1500 rating)\n"
            "`/lichessarena` (Shows all open tournaments)"
        ),
        "lichess_arena_no_data": "⚠️ Could not retrieve Lichess.org arena data.",
        "language_set": "✅ Language set to English!",
        "about": (
            "👋 Hi! I'm the *ChessCast* bot, your personal chess assistant. ♟️\n\n"
            "I bring you **daily chess facts**, **puzzles**, **real-time tournament updates** and **interesting pictures about chess** "
            "from *Lichess.org* and *Chess.com*. Want to check your chess stats? Just type your username and get instant ratings & game history! 🎯\n\n"
            "📌 **What can I do?**\n\n"
            "♟️ **Daily Chess Facts:**\n"
            "/start - Activate the bot and get your first chess fact\n\n"
            "♟️ **Tournaments & Players:**\n"
            "/lichessprofile `<username>` - View a Lichess.org player profile\n"
            "/lichessarena `<userrank>` - View open tournaments on Lichess\n"
            "/chessprofile `<username>` - View a Chess.com player profile\n\n"
            "♟️ **Notifications & Management:**\n"
            "/unsubscribe - Stop notifications and unsubscribe\n"
            "/about - Learn about the bot\n"
            "/language - Change bot language\n\n"
            " *Our official telegram channel 👇🏻*\n"
            "🔗 [For all updates](https://t.me/chesscast)\n\n"
            " *Want to play chess with me*\n"
            "🤝🏻 [Profile](https://lichess.org/@/StrongJunior)\n\n"
        ),
    },
    "ru": {
        "daily_chess_images": "📷 Дневные шахматные изображения здесь! Используйте как обои или поделитесь с друзьями! 🏆♟️",
        "puzzle_message": (
            "♟️ **Ежедневная шахматная головоломка**\n\n"
            "🔗 [Решите головоломку здесь]({url})\n"
            "📊 Сложность: {rating} Elo\n"
            "👀 Играна: {plays} раз(а)"
        ),
        "puzzle_error": "⚠️ Не удалось получить ежедневную головоломку. Попробуйте позже.",
        "set_rating_usage": (
            "⚠️ Пожалуйста, введите свое имя пользователя на Chess.com или Lichess.org.\n\n"
            "✅ Правильное использование:\n"
            "`/setrating StrongJunior`"
        ),
        "topplayers_header": "🏆 **Лучшие шахматисты по рейтингу**",
        "topplayers_no_data": "⚠️ Пока никто не установил свой рейтинг.",
        "set_rating_not_found": "❌ Пользователь `{username}` не найден или у него нет рейтинга.",
        "set_rating_success": "✅ Рейтинг `{username}` успешно установлен: `{rating}`.",
        "no_top_players": "⚠️ Пока никто не установил свой рейтинг.",
        "top_players_header": "🏆 **Топ игроков по рейтингу:**",
        "rating_user_not_found": "❌ Этот пользователь не найден на Chess.com или Lichess.org.",
        "rating_not_found": "⚠️ Рейтинг пользователя не найден.",
        "rating_set_success": "✅ Ваш рейтинг успешно установлен: `{rating}`",
        "lichess_profile_usage": "⚠️ Введите имя пользователя. Пример: `/lichessprofile StrongJunior`",
        "lichess_profile_not_found": "❌ Пользователь `{}` не найден.",
        "lichess_profile_header": "📊 **Информация о профиле Lichess.org**: `{}`\n\n",
        "chess_profile_usage": "⚠️ Введите имя пользователя. Пример: `/chessprofile shakhriyar-mamedyarov`",
        "chess_profile_not_found": "❌ Пользователь `{}` не найден.",
        "chess_profile_header": "📊 **Информация о профиле Chess.com**: `{}`\n\n",
        "rating_bullet": "♞ **Bullet рейтинг**: {}",
        "rating_blitz": "♞ **Blitz рейтинг**: {}",
        "rating_rapid": "♞ **Rapid рейтинг**: {}",
        "rating_daily": "♞ **Daily рейтинг**: {}",
        "total_games": "📌 **Всего игр**: {}",
        "games_won": "🔥 **Выигранные игры**: {} ({}%)",
        "games_lost": "❌ **Проигранные игры**: {}",
        "games_drawn": "🤝🏻 **Ничейные игры**: {}",
        "view_profile": "👀 **Посмотреть профиль**: [Нажмите здесь]({})",
        "donate_message": (
            "☕ **Даже будучи ботом, я люблю кофе!😒 **\n\n"
            "Если вам нравится мой бот и вы хотите поддержать его, "
            "можете угостить меня чашечкой кофе. 😌\n\n"
            "👉 [Поддержать меня здесь!](https://buymeacoffee.com/thehormat)"
        ),
        "unsubscribe_success": "❌ Вы отписались. Вы больше не будете получать шахматные факты. Не попадайтесь на глаза Каспарову...",
        "unsubscribe_already": "⚠️ Вы уже отписаны!",
        "start_welcome": "✅ Добро пожаловать, мой друг! Теперь каждый день ты будешь получать интересные и познавательные шахматные факты. Таль был бы тобой горд! ♟️",
        "start_already_registered": "🔹 Вы уже зарегистрированы! Шахматные любители ценят вашу страсть. ♟️",
        "lichess_arena_header": "🏆 **Активные турниры Lichess.org:**\n\n",
        "lichess_arena_no_tournaments": "❌ Для этого рейтинга турниров не найдено.",
        "lichess_arena_starts_in": "(Начало через {} мин)",
        "lichess_arena_error": (
            "⚠️ **Ошибка!** Рейтинг должен быть числом.\n\n"
            "✅ Правильное использование:\n"
            "`/lichessarena 1500` (Показывает турниры для рейтинга 1500)\n"
            "`/lichessarena` (Показывает все открытые турниры)"
        ),
        "lichess_arena_no_data": "⚠️ Не удалось получить данные арены Lichess.org.",
        "language_set": "✅ Язык изменен на русский!",
        "about": (
            "👋 Привет! Я *ChessCast* бот, твой личный шахматный помощник. ♟️\n\n"
            "Я предлагаю **ежедневные шахматные факты**, **головоломки**, **обновления турниров в реальном времени** и **интересные шахматные изображения** "
            "из *Lichess.org* и *Chess.com*. Хочешь узнать свой шахматный рейтинг? Просто введи свое имя пользователя и получи мгновенную статистику! 🎯\n\n"
            "📌 **Что я умею?**\n\n"
            "♟️ **Ежедневные шахматные факты:**\n"
            "/start - Активировать бота и получить первый шахматный факт\n\n"
            "♟️ **Турниры и игроки:**\n"
            "/lichessprofile `<username>` - Просмотр профиля игрока на Lichess.org\n"
            "/lichessarena `<userrank>` - Просмотр открытых турниров на Lichess\n"
            "/chessprofile `<username>` - Просмотр профиля игрока на Chess.com\n\n"
            "♟️ **Уведомления и управление:**\n"
            "/unsubscribe - Остановить уведомления и отписаться\n"
            "/about - Узнать больше о боте\n"
            "/language - Изменить язык бота\n\n"
            " *Наш официальный канал в телеграме 👇🏻*\n"
            "🔗 [Для всех обновлений](https://t.me/chesscast)\n\n"
            "*Хочешь сыграть со мной в шахматы*\n"
            "🤝🏻 [Профиль](https://lichess.org/@/StrongJunior)\n\n"
        ),
    },
    "tr": {
        "daily_chess_images": "📷 Günün satranç resimleri burada! Duvar kağıdı olarak kullan veya arkadaşlarınla paylaş! 🏆♟️",
        "puzzle_message": (
            "♟️ **Günün Satranç Bulmacası**\n\n"
            "🔗 [Buradan çöz]({url})\n"
            "📊 Zorluk: {rating} Elo\n"
            "👀 Oynanma sayısı: {plays}"
        ),
        "puzzle_error": "⚠️ Günlük bulmaca getirilemedi. Lütfen daha sonra tekrar dene.",
        "set_rating_usage": (
            "⚠️ Lütfen Chess.com veya Lichess.org kullanıcı adınızı girin.\n\n"
            "✅ Doğru kullanım:\n"
            "`/setrating StrongJunior`"
        ),
        "topplayers_header": "🏆 **En Yüksek Reytingli Satranç Oyuncuları**",
        "topplayers_no_data": "⚠️ Henüz hiçbir kullanıcı reyting belirlemedi.",
        "set_rating_not_found": "❌ Kullanıcı `{username}` bulunamadı veya reyting bilgisi mevcut değil.",
        "set_rating_success": "✅ `{username}` kullanıcısının reytingi başarıyla kaydedildi: `{rating}`.",
        "no_top_players": "⚠️ Henüz hiçbir kullanıcı reyting belirlemedi.",
        "top_players_header": "🏆 **En Yüksek Reytingli Oyuncular:**",
        "rating_user_not_found": "❌ Bu kullanıcı Chess.com veya Lichess.org üzerinde bulunamadı.",
        "rating_not_found": "⚠️ Bu kullanıcının reyting bilgisi mevcut değil.",
        "rating_set_success": "✅ Reytingin başarıyla kaydedildi: `{rating}`",
        "lichess_profile_usage": "⚠️ Kullanıcı adı girin. Örnek: `/lichessprofile StrongJunior`",
        "lichess_profile_not_found": "❌ Kullanıcı `{}` bulunamadı.",
        "lichess_profile_header": "📊 **Lichess.org Profil Bilgisi**: `{}`\n\n",
        "chess_profile_usage": "⚠️ Kullanıcı adı girin. Örnek: `/chessprofile shakhriyar-mamedyarov`",
        "chess_profile_not_found": "❌ Kullanıcı `{}` bulunamadı.",
        "chess_profile_header": "📊 **Chess.com Profil Bilgisi**: `{}`\n\n",
        "rating_bullet": "♞ **Bullet Reytingi**: {}",
        "rating_blitz": "♞ **Blitz Reytingi**: {}",
        "rating_rapid": "♞ **Rapid Reytingi**: {}",
        "rating_daily": "♞ **Günlük Reyting**: {}",
        "total_games": "📌 **Toplam oyun sayısı**: {}",
        "games_won": "🔥 **Kazandığı oyunlar**: {} ({}%)",
        "games_lost": "❌ **Kaybettiği oyunlar**: {}",
        "games_drawn": "🤝🏻 **Berabere kaldığı oyunlar**: {}",
        "view_profile": "👀 **Profili görüntüle**: [Buraya tıkla]({})",
        "donate_message": (
            "☕ **Ben bir bot olsam da kahveyi seviyorum!😒 **\n\n"
            "Eğer beni beğendiysen ve destek olmak istersen, "
            "bana küçük bir kahve ısmarlayabilirsin. 😌\n\n"
            "👉 [Buradan destek ol!](https://buymeacoffee.com/thehormat)"
        ),
        "unsubscribe_success": "❌ Bildirimlerden çıkış yaptınız. Artık satranç bilgileri almayacaksınız. Kasparov'a yakalanmayın...",
        "unsubscribe_already": "⚠️ Zaten bildirimlerden çıktınız!",
        "start_welcome": "✅ Hoş geldin dostum! Artık her gün ilginç ve eğitici satranç bilgileri alacaksın. Tal seninle gurur duyardı! ♟️",
        "start_already_registered": "🔹 Zaten kayıtlısınız! Satranç severler tutkunuzu takdir ediyor. ♟️",
        "lichess_arena_header": "🏆 **Lichess.org Canlı Turnuvalar:**\n\n",
        "lichess_arena_no_tournaments": "❌ Bu reyting için uygun turnuva bulunamadı.",
        "lichess_arena_starts_in": "(Başlamasına {} dakika kaldı)",
        "lichess_arena_error": (
            "⚠️ **Hata!** Reyting bir sayı olmalıdır.\n\n"
            "✅ Doğru kullanım:\n"
            "`/lichessarena 1500` (1500 reyting için turnuvaları gösterir)\n"
            "`/lichessarena` (Tüm açık turnuvaları gösterir)"
        ),
        "lichess_arena_no_data": "⚠️ Lichess.org turnuva bilgileri alınamadı.",
        "language_set": "✅ Dil Türkçe olarak ayarlandı!",
        "about": (
            "👋 Merhaba! Ben *ChessCast* botuyum, kişisel satranç asistanın! ♟️\n\n"
            "Sana **günlük satranç bilgileri**, **bulmacalar**, **canlı turnuva güncellemeleri** ve **ilginç satranç resimleri** getiriyorum. "
            "*Lichess.org* ve *Chess.com* veritabanlarını kullanarak anlık oyuncu reytingleri ve oyun geçmişlerini görüntüleyebilirsin! 🎯\n\n"
            "📌 **Ben neler yapabilirim?**\n\n"
            "♟️ **Günlük Satranç Bilgileri:**\n"
            "/start - Botu başlat ve ilk satranç bilginizi al\n\n"
            "♟️ **Turnuvalar & Oyuncular:**\n"
            "/lichessprofile `<kullanıcı_adı>` - Lichess.org oyuncu profilini görüntüle\n"
            "/lichessarena `<reyting>` - Lichess'teki açık turnuvaları görüntüle\n"
            "/chessprofile `<kullanıcı_adı>` - Chess.com oyuncu profilini görüntüle\n\n"
            "♟️ **Bildirimler & Yönetim:**\n"
            "/unsubscribe - Bildirimleri durdur ve aboneliği iptal et\n"
            "/about - Bot hakkında bilgi al\n"
            "/language - Bot dilini değiştir\n\n"
            " *Resmi telegram kanalımız 👇🏻*\n"
            "🔗 [Tüm güncellemeler için](https://t.me/chesscast)\n\n"
            " *Benimle satranç oynamak ister misin*\n"
            "🤝🏻 [Profilim](https://lichess.org/@/StrongJunior)\n\n"
        ),
    },
}


GPT_PROMPTS = {
    "az": (
        "Sən bir şahmat bilicisisən və insanlara şahmat haqqında "
        "maraqlı, öyrədici və nadir məlumatlar təqdim edirsən. "
        "İstifadəçilərə şahmat strategiyaları, açılışlar, şahmat daşları, şahmat tarixi və məşhur şahmatçılar haqqında qısa, "
        "amma detallı və təsirli faktlar ver. **Amma cavabında yalnız 1 və ya maksimum 2 fakt olmalıdır.**\n\n"
        "**Format:**\n"
        "- Hər faktın əvvəlində `♟️` emojisi olmalıdır.\n"
        "- **Başlıq bu formada yazılmalıdır: `♟️ **Şahmat Taxtasının Tarixi**`**\n"
        "- Faktın izahı isə normal mətndə olmalıdır.\n"
        "- Bütün faktlar **təmiz və düzgün Azərbaycan dilində yazılmalıdır**.\n"
        "- Faktlar **çox uzun olmamalıdır**, maksimum 4-5 cümlə ilə izah edilməlidir.\n"
        "- Cavabın **tam olmalıdır və yarımçıq qalmamalıdır!**\n\n"
        "**Nümunə:**\n"
        "`♟️ **Şahmat Taxtasının Tarixi**`\n"
        "Şahmat oyununun kökləri 6-cı əsr Hindistanına qədər uzanır. İlk adı 'Çaturanga' olan bu oyun, "
        "Fars və Avropa mədəniyyətlərinə yayılaraq indiki şahmat formasını almışdır.\n\n"
        "`♟️ **Məşhur Ruy Lopez Açılışı**`\n"
        "Bu açılış, ispan şahmat ustası Ruy López tərəfindən yaradılmışdır və strateji üstünlük verməsi ilə tanınır."
    ),
    "en": (
        "You are a chess expert providing users with interesting and educational chess facts. "
        "Your task is to generate short but insightful facts about chess strategies, openings, pieces, history, and famous players. "
        "**However, your response should contain only 1 or at most 2 facts.**\n\n"
        "**Format:**\n"
        "- Each fact must start with `♟️` emoji.\n"
        "- **Title format should be like this: `♟️ **The History of Chessboard**`**\n"
        "- The explanation of the fact should be written in normal text.\n"
        "- All facts must be **clear and well-written in English**.\n"
        "- Facts should not be **too long**, maximum 4-5 sentences.\n"
        "- The response **must be complete and not cut off**.\n\n"
        "**Example:**\n"
        "`♟️ **The History of Chessboard**`\n"
        "The origins of chess trace back to 6th-century India, where it was first called 'Chaturanga'. "
        "It later spread to Persia and Europe, evolving into the modern game we know today.\n\n"
        "`♟️ **The Famous Ruy Lopez Opening**`\n"
        "This opening was developed by Spanish chess master Ruy López in the 16th century. It is known for its strategic depth."
    ),
    "ru": (
        "Вы - эксперт по шахматам, предоставляющий пользователям интересные и познавательные факты о шахматах. "
        "Ваша задача - генерировать короткие, но содержательные факты о шахматных стратегиях, дебютах, фигурах, истории и знаменитых игроках. "
        "**Однако ваш ответ должен содержать только 1 или максимум 2 факта.**\n\n"
        "**Формат:**\n"
        "- Каждый факт должен начинаться с эмодзи `♟️`.\n"
        "- **Формат заголовка должен быть таким: `♟️ **История шахматной доски**`**\n"
        "- Объяснение факта должно быть написано обычным текстом.\n"
        "- Все факты должны быть **четкими и грамотно написанными на русском языке**.\n"
        "- Факты не должны быть **слишком длинными**, максимум 4-5 предложений.\n"
        "- Ответ **должен быть полным и не обрываться**.\n\n"
        "**Пример:**\n"
        "`♟️ **История шахматной доски**`\n"
        "Шахматы берут свое начало в VI веке в Индии, где они назывались 'Чатуранга'. "
        "Позже игра распространилась в Персию и Европу, превратившись в современный вариант, который мы знаем сегодня.\n\n"
        "`♟️ **Знаменитый дебют Руй Лопеса**`\n"
        "Этот дебют был разработан испанским шахматным мастером Руй Лопесом в XVI веке. Он известен своей стратегической глубиной."
    ),
    "tr": (
        "Sen bir satranç uzmanısın ve kullanıcılara satranç hakkında ilginç ve eğitici bilgiler sağlıyorsun. "
        "Görevin, satranç stratejileri, açılışlar, taşlar, tarih ve ünlü oyuncular hakkında kısa ama öğretici bilgiler üretmektir. "
        "**Ancak, cevabın yalnızca 1 veya en fazla 2 bilgi içermelidir.**\n\n"
        "**Format:**\n"
        "- Her bilgi `♟️` emojisi ile başlamalıdır.\n"
        "- **Başlık formatı şu şekilde olmalıdır: `♟️ **Satranç Tahtasının Tarihi**`**\n"
        "- Bilginin açıklaması normal metinle yazılmalıdır.\n"
        "- Tüm bilgiler **Türkçe olarak açık ve anlaşılır bir şekilde yazılmalıdır**.\n"
        "- Bilgiler **çok uzun olmamalıdır**, maksimum 4-5 cümle içermelidir.\n"
        "- Cevap **tam olmalı ve kesilmemelidir**.\n\n"
        "**Örnek:**\n"
        "`♟️ **Satranç Tahtasının Tarihi**`\n"
        "Satranç, kökenlerini 6. yüzyılda Hindistan'a kadar dayandırır. İlk olarak 'Çaturanga' olarak adlandırılmış, "
        "daha sonra Pers ve Avrupa'ya yayılarak bugünkü modern satranç haline gelmiştir.\n\n"
        "`♟️ **Ünlü Ruy Lopez Açılışı**`\n"
        "Bu açılış, 16. yüzyılda İspanyol satranç ustası Ruy López tarafından geliştirilmiştir. Stratejik derinliği ile tanınır."
    ),
}
