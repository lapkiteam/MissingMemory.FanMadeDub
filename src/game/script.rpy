# Вы можете расположить сценарий своей игры в этом файле.

image beach = "Beach.png"
image umbrella = "Umbrella.png"
image adalinda happy = "characters/Adalinda.png"
image horizont = "Horizont.png"

# Определение персонажей игры.
define n = Character()
define p = Character("Павел", color="#2EA586")
define w = Character("Незнакомка", color="#BF4963")
define horizont = Character("Ведущий", color="#4C81E5")

define Pavel = Character('Павел', color="#249351")
define Something = Character('Незнакомка', color="#9E3E95")

define audio.Warmly = "music/Warmly_Memories.mp3"

image playing_video = "images/PlayingVideo.png"
image our_answer = "images/OurAnswer.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а adalinda happy — "adalinda happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    jump original_scene_on_beach
    # jump our_scene

label original_scene_on_beach:
    stop music fadeout 3.0
    play music Warmly volume 0.5

    scene black
    show text Text(
        "Одним скучным вечерком\nмы наткнулись на озвучку Missing Memory…",
        size = 40,
        textalign = 0.5,
        color = "#ffffff",
    )
    with dissolve
    pause 7

    scene playing_video with dissolve

    voice "voices/p-1_130.ogg"
    "Как давно я не ощущал этой мягкости..."

    # voice "voices/p-1_131.ogg"
    # "Что за?"
    voice "voices/p-1_132.ogg"
    "Пляж?"
    # voice "voices/p-1_133.ogg"
    # "Откуда?"
    # voice "voices/p-1_134.ogg"
    # "Как я попал сюда?"
    # voice "voices/p-1_135.ogg"
    # "Хотя... Как давно я не был тут."
    # voice "voices/p-1_136.ogg"
    # "Надо будет когда-нибудь снова сюда поехать."
    show black as half_dark:
        alpha 0.1
    voice "voices/So1_01.ogg"
    Something "Ты случайно не уснул?"
    show black as half_dark:
        alpha 0.2
    voice "voices/p-1_137.ogg"
    "Прозвучал чей-то голос..."
    # voice "voices/p-1_138.ogg"
    # "Голос девушки."
    # voice "voices/p-1_139.ogg"
    # "Добрый, но какой-то знакомый..."
    # Pavel "Нет, не сплю."
    # voice "voices/So1_02.ogg"
    # Something "Это хорошо, я ведь не хочу, чтобы у тебя был солнечный удар."
    show black as half_dark:
        alpha 0.3
    voice "voices/So1_03.ogg"
    Something "Сейчас зонтик принесу."
    show black as half_dark:
        alpha 0.4
    voice "voices/p-1_140.ogg"
    "Кто это был?"
    # voice "voices/p-1_141.ogg"
    # "Точнее, кто она и откуда меня знает?"
    show black as half_dark:
        alpha 0.5
    voice "voices/p-1_142.ogg"
    "Незнакомка всё же пришла с зонтиком."
    # voice "voices/So1_04.ogg"
    # Something "Ну теперь не должно быть жарко."
    # voice "voices/p-1_143.ogg"
    # "Она села передо мной."
    # voice "voices/p-1_144.ogg"
    # "Её лицо не было видно, только её улыбка."
    # voice "voices/p-1_145.ogg"
    # "Она улыбалась..."
    # voice "voices/So1_05.ogg"
    # Something "Будешь дальше лежать или пойдем к воде?"
    # Pavel "Нет, я ещё полежу."
    show black as half_dark:
        alpha 0.6
    voice "voices/So1_06.ogg"
    Something "Я рядом буду если что, хорошо?"
    # Pavel "Хорошо"
    show black as half_dark:
        alpha 0.7
    voice "voices/p-1_146.ogg"
    "Она покинула мой взор, остался только я и горизонт."

    hide half_dark
    stop music
    play sound "sfx/record-scratch-wut.mp3"
    "..."

    scene our_answer with dissolve
    pause 5

    jump our_scene

label our_scene:
    play music "music/outscout – Whistle Of Sailman HenrySera.mp3" fadein 1.0 volume 0.1

    scene black
    show text Text(
        "Many hours later…",
        size = 40,
        textalign = 0.5,
        color = "#ffffff",
    )
    with dissolve
    pause 3

    scene black
    with dissolve

    voice "voices/n-01.mp3"
    n "Как давно я не ощущал этой мягкости. Либо песок, либо я уже в гробу с мягкой подложкой."

    scene beach with dissolve

    voice "voices/n-02.mp3"
    n "Что за?"
    voice "voices/n-03.mp3"
    n "Пляж?"
    voice "voices/n-04.mp3"
    n "Откуда? Надеюсь, не из военкомата."
    voice "voices/n-05.mp3"
    n "Как я попал сюда? И кто оплатил дорогу? Лучше не думать."
    voice "voices/n-06.mp3"
    n "Хотя… Как давно я не был тут?"
    voice "voices/n-07.mp3"
    n "Надо будет когда-нибудь снова сюда поехать. Сказал человек, который уже несколько лет пишет вторую главу визуальной новеллы, хех."

    show adalinda happy
    with dissolve

    voice "voices/w-ты не уснул 4.mp3"
    w "Ты случайно не уснул?" with dissolve
    voice "voices/n-08.mp3"
    n "Прозвучал чей-то голос."
    voice "voices/n-09.mp3"
    n "Голос девушки."
    voice "voices/n-10.mp3"
    n "Добрый, но какой-то знакомый… голос автоответчика или нет? Если предложат взять кредит, то всё-таки автоответчик."
    voice "voices/p-1.mp3"
    p "Нет, не сплю."
    voice "voices/w-это хорошо3.mp3"
    w "Это хорошо. А то я хотела тебе усики подрисовать."
    voice "voices/w-сейчас зонтик принесу5.mp3"
    w "Сейчас зонтик принесу, чтобы ты от солнечного удара не помер."
    hide adalinda happy
    with dissolve
    voice "voices/n-11.mp3"
    n "Кто это был?"
    voice "voices/n-12.mp3"
    n "Точнее, кто она и откуда знает? Блин, версия с военкоматом всё больше меня беспокоит."
    show umbrella
    show adalinda happy
    with dissolve
    voice "voices/n-13.mp3"
    n "Незнакомка всё же пришла с зонтиком. Нет, военкомат бы не стал так стараться."
    voice "voices/w-но теперь не должно быть жарко4.mp3"
    w "Но теперь не должно быть жарко."
    voice "voices/n-14.mp3"
    n "Она села передо мной."
    voice "voices/n-15.mp3"
    n "Ее лица не было видно, только ее улыбка."
    voice "voices/n-16.mp3"
    n "Она улыбалась."
    voice "voices/w-будешь дальше лежать5.mp3"
    w "Будешь дальше лежать или пойдем к воде?"
    voice "voices/p-2.mp3"
    p "Нет, я еще полежу. Я ещё горизонтом не насладился!"
    voice "voices/w-я рядом буду4.mp3"
    w "Я рядом буду если что, хорошо?"
    voice "voices/p-3.mp3"
    p "Хорошо."
    hide adalinda happy
    with dissolve
    voice "voices/n-17.mp3"
    n "Она покинула мой взор, как и всё хорошее в последнее время. Остался только я и…"

    voice "voices/news.mp3"
    show horizont
    horizont "Экстренные новости! Молодой парень пропал посреди города. Полиция ищет…" with dissolve

    voice "voices/n-18.mp3"
    n "Ну и нафиг мне этот «Горизонт» сдался?!"

    scene black
    show text Text(
        "Конец!",
        size = 40,
        textalign = 0.5,
        color = "#ffffff",
    )
    pause 5
