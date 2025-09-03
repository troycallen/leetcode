class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS = len(img)
        COLS = len(img[0])
        prev_row = img[0][:]

        for r in range(ROWS):
            curr_row = img[r][:]
            for c in range(COLS):
                total = 0
                cnt = 0
                for i in range(max(0, r - 1), min(ROWS, r + 2)):
                    for j in range(max(0, c - 1), min(COLS, c + 2)):
                        if i == r:
                            total += curr_row[j]
                        elif i == r - 1:
                            total += prev_row[j]
                        else:
                            total += img[i][j]
                        
                        cnt += 1
                img[r][c] = total // cnt
            
            prev_row = curr_row
        return img

        