# Usage
1. Copy `beamercolorthemeppt_theme_1.sty`, `beamerfontthemeppt_theme_1.sty`, `beamerinnerthemeppt_theme_1.sty`, `beamerouterthemeppt_theme_1.sty` and `beamerthemeppt_theme_1.sty` in the same directory as your project `.tex` file.

2. Add the following in preamble.
   ```
   \usepackage{changepage}
   \usepackage[style=verbose,giveninits=true]{biblatex}
   \usepackage{csquotes}
   \usepackage{amsmath}
   \usepackage{amssymb}
   \usepackage{mathtools}
   \usepackage{MnSymbol}

   \usetheme{ppt_theme_1}
   \usefonttheme[onlymath]{serif}
   ```

# Preview
![Alt text](/preview/0.svg)
![Alt text](/preview/1.svg)
![Alt text](/preview/2.svg)
![Alt text](/preview/3.svg)
![Alt text](/preview/4.svg)
![Alt text](/preview/5.svg)

# Inspirations
* https://github.com/sano-jin/express-beamer
* https://github.com/NicklasXYZ/NXYZBeamerTheme
