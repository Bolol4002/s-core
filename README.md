# s-core
my nth attempt in building a cpu

## Components used within this architecture.
- A register fiel
- An instruction memory
- some data memory
- a sign extender
- a bsic alue
- decoder/control unit 

![architecture](img/architecture.jpg)

---

# Memory.sv file
- We create a byte adressed memory file which can fetch data in one clock cycle ideally 
- The difference is what each memory address refers to.
    - Byte-addressed memory: each address points to 1 byte (8 bits).
    - Word-addressed memory: each address points to 1 word (e.g., 32 bits or 64 bits, depending on the architecture).
