class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #想要回到原点  向左的步数等于向右的步数  向上的步数等于向下的步数
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False
