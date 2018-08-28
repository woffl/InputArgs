# InputArgs
A sublime text plugin to send custom input arguments when building using "ctrl+B". View a program output with custom arguments from within sublime text.


## Installing

### OSX

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
$ git clone git://github.com/woffl/InputArgs.git InputArgs

```

### Linux (Ubuntu like distros)

```
$ cd ~/.config/sublime-text-3/Packages/
$ git clone git://github.com/woffl/InputArgs.git InputArgs

```

### Windows

```
Copy the directory to: "C:\Users\<username>\AppData\Roaming\Sublime Text 3\Packages"

```


## Usage

You must create a custom Build System to enable asking for input arguments via the option `"ask_input_args": true`. New Build Systems can be added through "Tools>Build System>New Build System".

The plugin includes an example for the Python Build System, which extends the original Python Build System. When building a Python file for the first time or when pressing "ctrl+shift+B", you can choose between normal "Python" (without input arguments) and "Python - Input Args" (with input arguments). When choosing the second, an input dialog will open and ask for input arguments. Pressing "ctrl+B" retains the last choice for subsequent builds.

While the input dialog is open, you can use the up and down arrow keys to scroll through the history of input arguments.


## Credits and license

Thank you to the authors of Sublime Text for making such a beautiful text editor with such a powerful plugin API. Thank you, [bilalba](/bilalba), for making the original InputArgs and sharing its source.

Most of the code in this repository is either a copy from the original exec.py included in Sublime Text or a copy from the original InputArgs plugin. I hereby put the few lines that I contributed myself in the public domain.
