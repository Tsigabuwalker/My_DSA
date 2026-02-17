class Solution:
    def rearrangeBarcodes(self, barcodes):
        
        from collections import Counter
        
        n = len(barcodes)
        count = Counter(barcodes)
        
        # Sort barcodes by frequency descending
        sorted_barcodes = sorted(count.items(), key=lambda x: -x[1])
        
        res = [0] * n
        i = 0  # even index
        
        # Place barcodes in order of frequency
        for barcode, freq in sorted_barcodes:
            for _ in range(freq):
                res[i] = barcode
                i += 2
                if i >= n:
                    i = 1  # move to odd index after filling even
        
        return res
