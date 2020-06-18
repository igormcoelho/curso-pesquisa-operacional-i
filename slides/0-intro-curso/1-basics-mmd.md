------------------------------------------------------------------------

author: Igor M. Coelho title: Demonstration Beamer/Reveal date: April 8,
2020 transition: cube fontsize: 10 header-includes: -
`<link rel="stylesheet" type="text/css" href="general.css">`{=html} -
`<link rel="stylesheet" type="text/css" href="reveal-beamer.css">`{=html}
\-\--

Part 1: Basics
==============

------------------------------------------------------------------------

Basic Formatting {.allowframebreaks}
------------------------------------

Text
`<span latex-color="blue" style="color:blue">`{=html}formatting`</span>`{=html}
requires a few things, such as lists (prefix `-`, `*` or `+`):

-   **bold** (Markdown `**bold**`, LaTeX `\textbf{bold}`)
-   *italics* (Markdown `*italics*`, LaTeX `\textit{italics}`)
    -   ***bold and italics*** (Markdown `***` symbol, LaTeX
        `\textbf{\textit{...}}`)

Enumeration lists can use `1.` or `#.` prefix:

1.  one
2.  two

::: {.block}

### An important reminder for $\text{\LaTeX}$

Use `<span latex-color="red" style="color: red;">`{=html}math
mode`</span>`{=html} as `$\sum_{i=0}^{n}\sqrt{i}$` for
$\sum_{i=0}^{n}\sqrt{i}$.

:::

For color use \"`--filter pandoc-latex-color`\": then use
`<span latex-color="green" style="color:green;">abc</span>`.

------------------------------------------------------------------------

Headers and Tables {\#header-tables}
------------------------------------

Headers can become different things (e.g,`--slide-level 2` on Pandoc):

  Slide     Header 1 (`#`)                   Header 2 (`##`)    Header 3 (`###`)
  --------- ------------------------------- ----------------- ------------------
  Level 1   Frame                                  Box        
  Level 2   Section `<br>`{=html} Section         Frame                      Box
  Level 3   Section                            Subsection                  Frame

You just need to use standard markdown table notation:

\\footnotesize

    | Slide   | Header 1 (`#`) | Header 2 (`##`) | Header 3 (`###`) |
    | :---    |    :----       |         :---:   |          ---:    |
    | Level 1 | Frame          | Box                               ||
    | Level 2 | Section        | Frame           | Box              |
    | Level 3 | Section        | Subsection      | Frame            |

------------------------------------------------------------------------

Images {\#sec-images1}
----------------------

To insert figures in slide, you can use Markdown notation:
`![AltText](./filename.jpg "Title")`

To resize it and visualize on Atom, Beamer and Reveal, just use Pandoc
`bracketed_spans` notation: `{width=80%}`.

![An universe picture](./universe.jpg "An example image"){width=30%}

Example:
`![An universe picture](./universe.jpg "An example image"){width=40%}`

------------------------------------------------------------------------

Organization and Columns (Part I)
---------------------------------

Let\'s divide in three parts (35%, 30%, 35%):

```{=html}
<div class="columns">
<div class="column" width="35%" style="max-width:35%;">

- First column
  - Some item
</div>
<div class="column" width="30%" style="max-width:30%;">

**Just an equation:** $$\sum_{i=0}^{n}\sqrt{i}$$
</div>
<div class="column" width="35%" style="max-width:35%;">

1. A third column
   * Something
1. One extra item
</div>
</div>
```
*To create multiple columns in a compatible way, we can use:*
\\footnotesize

``` {.html}
<div class="columns">
  <div class="column" width="35%" style="max-width:35%;">
     Content for column with 35% size
  </div>
</div>
```

------------------------------------------------------------------------

Fenced Divss {\#fenceddivs}
---------------------------

```{=html}
<!-- not working on typora nor Atom yet -->
```
This code should allow organizing text into column.

::::::::::::: {.columns}

::::: {.column width=100%}

::: {.centered}

\\centering

*Single centered column*

:::

:::::

:::::::::::::

    ::::::::::::: {.columns}
    ::::: {.column width=100%}
    ::: {.centered}
    \centering
    *Single centered column*
    :::
    :::::
    :::::::::::::

This doesn\'t work on Typora or Atom, but works on LaTeX and Reveal.

For centering, just `::: {.centered}` and `\centering` would be enough.

------------------------------------------------------------------------

Organization and Columns (Part II)
----------------------------------

Double column with image on side (20% and 80%):

```{=html}
<div class="columns">
<div class="column" width="50%" style="max-width:50%;">

- One topic
  - Another item
- Second topic
  - One extra
    - One deeper level

</div>
<div class="column" width="50%" style="max-width:50%;">

<style> img[alt="An universe picture"] { width: 70%; } </style>
![An universe picture](./universe.jpg "An example image"){width=70%}

</div>
</div>
```
### Fenced Divs

Note that Pandoc 2.9 provides a special syntax for fenced divs, like:
`::::::: {.columns}` and `::: {.column width="50%"}`. This is not
recommended because Atom Preview will not understand it. For the same
reason, use both `max-width=50%;` and `width="50%"`.

`<br/>`{=html}`<br/>`{=html}`<br/>`{=html}`<br/>`{=html}

------------------------------------------------------------------------

Some notes
----------

```{=html}
<div class="notes right">
```
These notes are not on main slide.

-   You can use `<div class="notes">`
-   Or right-align: `<div class="notes right">`
    ```{=html}
    </div>
    ```

This slide will only ask you to press `s` on Reveal. This will put you
on `Speaker Mode` and you\'ll see the notes.

### For Beamer

This is more complicated, but possible. It requires an specialized `pdf`
player for multiple monitors, like `pdfpc` or `pympress`.

    %\documentclass[notes]{beamer}       % frame + notes
    \documentclass[notes=only]{beamer}   % only notes
    %\documentclass{beamer}              % only frames

Thanks
======

------------------------------------------------------------------------

Last advices {\#hh-lastadvices}
-------------------------------

Never add frame breaks `------` before Level 1 headers (`#`). Otherwise
it will create a blank slide ;)

#### Practice on Atom, VSCode or Typora editors

On Atom, install one of these plugins: - Markdown Preview Plus:
`https://atom.io/packages/markdown-preview-plus` - Markdown Preview
Enhanced: `https://atom.io/packages/markdown-preview-enhanced`

`https://github.com/atom-community/markdown-preview-plus/wiki/markdown-it-vs.-pandoc`

::::::::::::: {.columns}

::::: {.column width=100%}

::: {.centered}

\\centering

***See you next time!***

:::

:::::

:::::::::::::

```{=html}
<!-- begin style part -->
```
```{=html}
<style>
    .reveal section p {
    display: block;
    text-align: justify;
    font-size: 0.68em;
    line-height: 1.2em;
    vertical-align: top;
    margin-left: 1em;
    margin-right: 0.5em;
  }
.reveal column p {
  margin-top: 0em;
  vertical-align: top;
}
.reveal section pre {
    font-size: 0.68em;
}
.reveal section code {
    font-size: 0.72em;
}
.reveal td,
.reveal th,
.reveal figcaption {
    font-size: 0.68em;
}
.reveal h2 {font-size: 1.5em; }
.reveal h3 {font-size: 1.0em; }
.reveal ol,
.reveal dl,
.reveal ul {
    display: block;
  text-align: left;
  font-size: 0.6em;
    margin: 0 0 0 3em;
}
.reveal ul ul {
  font-size: 1em;
}
</style>
```
```{=html}
<style type="text/css">
.columns {display:inline-flex;}
</style>
```
```{=html}
<style type="text/css">
.notes {color:red;}
.right {float:right;}
</style>
```
```{=html}
<style>
/* The switch - the box around the slider */
.switch {
 position: relative;
 display: inline-block;
 width: 60px;
 height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
 opacity: 0;
 width: 0;
 height: 0;
}

/* The slider */
.slider {
 position: absolute;
 cursor: pointer;
 top: 0;
 left: 0;
 right: 0;
 bottom: 0;
 background-color: #ccc;
 -webkit-transition: .4s;
 transition: .4s;
}

.slider:before {
 position: absolute;
 content: "";
 height: 26px;
 width: 26px;
 left: 4px;
 bottom: 4px;
 background-color: white;
 -webkit-transition: .4s;
 transition: .4s;
}

input:checked + .slider {
 background-color: #2196F3;
}

input:focus + .slider {
 box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
 -webkit-transform: translateX(26px);
 -ms-transform: translateX(26px);
 transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
 border-radius: 34px;
}

.slider.round:before {
 border-radius: 50%;
}
</style>
```
```{=html}
<!-- finished -->
```
