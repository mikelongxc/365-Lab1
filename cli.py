class CLI:
    def __init__(self):
        print("Enter a command followed by search options\n")
        self.print_help()

    def print_help(self):
        print("""usage: <command>: [<options>]
        
    commands:
        S[tudent]:  <lastname> [B[us]]
        T[eacher]:  <lastname>
        B[us]:  <number>
        G[rade]:  <number> [H[igh]|L[ow]]
        A[verage]:  <number>
        I[nfo]
        Q[uit]
                """)

