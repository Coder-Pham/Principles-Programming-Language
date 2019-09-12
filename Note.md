# Micro C LEXER - PARSER note

## Program Structure

- NO variable init (float i = 1.0;)
- NO **overloading** function
- NO **nested** function created
```
void foo(int i) {
    float child(float f) { ... }
}
```

## Lexical 

- \r \n \t blank => whitespace character
- COMMENTS => 0 TOKEN
    - FOUND // -> 0
    - FOUND /* until */ -> 0

### Token

- Identifiers:
    - Letters, digits, underscores
    - First must **letters** | **underscores**
    - Case sensitive

    **Note**: 'a123' should be 'a' - '123' or 'a123'.

- Keywords: () -> check ID for these words. 
    - boolean break continue else for float if int return void do while true false string
- Operators: **15 different**
    - Write 15 lexers (regex)
- Separators:
    - Define 6 brackets
    - Define colon and comma
- Literals
    - 