# Фанатская озвучка Missing Memory

Скачать [renpy-7.4.4-sdk](https://www.renpy.org/dl/7.4.4/renpy-7.4.4-sdk.zip) и распаковать куда-нибудь.

Запустить проект:

```bash
renpy src run
```

Скомпилировать проект:

```bash
renpy launcher distribute src --destination deploy --package pc
```

* `launcher` — это папка внутри RenPy. У меня она расположена тут — `/e/Portable/renpy-7.4.4-sdk/launcher`
* `--package pc` содержит и Windows версию и Linux
