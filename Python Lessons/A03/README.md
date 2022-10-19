## Project 03 - Decode / Encode

### Loic Konan

### Description

> This program will Write a codebreaker program that will use the key below to encode or decode a document.  
> You will be given an encrypted document to decode.
>
> - Key
> A = !
> E = @
> I = #
> O = $
> U = %
> a = ^
> e = &
> i = *
> o = (
> u = )
> S = +
> T = -
> d = >
> h = ;
> k = <
> n = :
> r = ]
> s = {
> t = =
> y = ]
> 
> All other characters will remain the same.
### Files

- File name infile.

```
F)::y st(]*&s f](m R&^>&]'s D*g&st.

W& w&]& g(*:g ()t (f st^t& f(] s*x w&&<s ^:> ^s<&> t;& :&*g;b(]s' :*:& y&^] (l> s(:, M*<&, 
t( c^]& f(] ()] >(g. W& &xpl^*:&> t;^t t;& j(b ]&q)*]&> f&&>*:g, g]((m*:g, w^l<*:g ^:>, 
m(st (f ^ll, pl&:ty (f l(v& ^:> pl^yt*m&. -;&: w& ^s<&> M*<& w;^t t;& j(b w()l> b& w(]t;
t( ;*m. "#'ll g*v& y() t&: b)c<s," ;& s^*>.

-;*s ;(t&l st*:<s, ^ g)&st c(mpl^*:&> w;&: ;& s;(w&> )p ^t t;& f](:t >&s< t( c;&c< ()t.  
W;^t's w](:g? # ^s<&>. # g(t :( sl&&p.  @v&]y 15 m*:)t&s t;*s l()> b^:g*:g s():> w(<& m& 
)p.  # ^p(l(g*z&> f(] t;& :(*s& ^:> c;&c<&> ;*m ()t.  ! f&w m*:)t&s l^t&], ^ c()pl& s;(w&>
)p.  !g^*:, # m^>& t;& m*st^<& (f ^s<*:g ;(w t;&*] st^y w^s. -&]]*bl&, t;&y s^*>.  -;& g)y
*: t;& :&xt ]((m w^s s:(]*:g s( l()>ly t;^t w& ;^> t( b^:g (: t;& w^ll &v&]y 15 m*:)t&s t( 
w^<& ;*m )p.

```

### Output Example
    
    ```
 
    ```
### Code
    
    ```python
    # Path: Python Lessons\A03\decode.py
    # Project 03 - Decode / Encode
    # Loic Konan
    # Description: This program will Write a codebreaker program that will use the key below to encode or decode a document.
    # You will be given an encrypted document to decode.
    # Key
    # A = !
    # E = @
    # I = #
    # O = $
    # U = %
    # a = ^
    # e = &
    # i = *
    # o = (
    # u = )
    # S = +
    # T = -
    # d = >
    # h = ;
    # k = <
    # n = :
    # r = ]
    # s = {
    # t = =
    # y = ]
    # All other characters will remain the same.

    # Open the file
    file = open("F)::y st(]*&s f](m R&^>&]'s D*g&st.", "r")

    # Read the file
    file_content = file.read()

    # Close the file
    file.close()

    # Create a dictionary

    key = {
        "A": "!",
        "E": "@",
        "I": "#",
        "O": "$",
        "U": "%",
        "a": "^",
        "e": "&",
        "i": "*",
        "o": "(",
        "u": ")",
        "S": "+",
        "T": "-",
        "d": ">",
        "h": ";",
        "k": "<",
        "n": ":",
        "r": "]",
        "s": "{",
        "t": "=",
        "y": "]"
    }

    # Create a new string
    new_string = ""

    # Loop through the string
    for char in file_content:
        if char in key:
            new_string += key[char]
        else:
            new_string += char

    # Print the new string
    print(new_string)
    ```

### RUN

```bash
python main.py
```

### Files

|   #   | File               | Description | Status                  |
| :---: | ------------------ | ----------- | ----------------------- |
|   1   | [main.py](main.py) | Solution    | :ballot_box_with_check: |
