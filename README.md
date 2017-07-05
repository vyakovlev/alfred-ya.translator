# Yandex Translator workflow for Alfred

Yet another Ya.Translator (aka Yandex.Translator) will help you to quickly translate to/from your native/desired language. Input language detection is automatic.

Workflow can be set up to use any language pair (e.g. Italian/French). English/Russian is set by default.

You can either translate a single word, e.g. "desire", or a sentence, e.g. "isn't it a great day?".

You can either trigger workflow by `t` and query (e.g. `t hello, world`) or use a shortcut to translate selection (see below).

Example:

![Query](https://vyakovlev.com/projects/alfred/ya.translator/query.png)

translates into the following and gets copied into clipboard

![Translation](https://vyakovlev.com/projects/alfred/ya.translator/translation.png)

# Installation

Make sure you have [Alfred Powerpack](https://buy.alfredapp.com/) to import this workflow.

Download the [workflow](https://vyakovlev.com/projects/alfred/ya.translator/Ya.Translator.alfredworkflow)

Import to Alfred

![import](https://vyakovlev.com/projects/alfred/ya.translator/import.png)

Set up APIKEY (you can get a free APIKEY from Yandex at https://tech.yandex.com/key/form.xml?service=trnsl): under [X] button on upper right corner in Alfred Workflow:

![setup-apikey](https://vyakovlev.com/projects/alfred/ya.translator/setup-apikey.png)

You can also choose a hotkey to translate text selection:

![setup-shortcut](https://vyakovlev.com/projects/alfred/ya.translator/setup-shortcut.png)

# Advanced configuration of languages key-pairs

Open Python script and change two variables, then save:

![advanced](https://vyakovlev.com/projects/alfred/ya.translator/advanced.png)

# Hooray!

You are done! Enjoy and don't hesitate to react me at i@vyakovlev.com in case of any difficulties.

P.S. I was inspired by [Michael Danilov](https://danilov.me) and his [workflow](https://github.com/MichaelDanilov/alfred-yatranslate).

## Licenses and agreements

MIT, 2017 [Vladimir Yakovlev](https://vyakovlev.com)

[Terms of Use of API Yandex.Translate Service](https://yandex.ru/legal/translate_api/) and Yandex.Translate logo © [Yandex](https://www.yandex.ru/)