class Solution:
    def reverse(self, x: int) -> int:
        output = str(x)[::-1]
        if output[-1] == "-":
            output = output[-1] + output[0:-1]
        final = int(output)
        if final > 2147483647 or final < -2147483648:
            return 0
        return final
