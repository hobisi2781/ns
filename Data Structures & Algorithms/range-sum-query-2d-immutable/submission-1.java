class NumMatrix {
    int[][] rowPrefixMatrix;
    int[][] matrix;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        this.rowPrefixMatrix = new int[m][n];
        this.matrix = matrix;

        for (int i = 0; i < m; i++) {
            int prefix = 0;
            for (int j = 0; j < n; j++) {
                prefix += matrix[i][j];
                this.rowPrefixMatrix[i][j] = prefix;
                // System.out.print("%d ".formatted(prefix));
            }
            // System.out.println("");
        }
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;

        for (int i = row1; i <= row2; i++) {
            // System.out.println("[i][col2]=%d, [i][col1]=%d, matrix-cell=%d, i=%d, col1=%d, col2=%d".formatted(rowPrefixMatrix[i][col2], rowPrefixMatrix[i][col1], matrix[i][col1], i, col1, col2));
            sum += rowPrefixMatrix[i][col2] - rowPrefixMatrix[i][col1] + matrix[i][col1]; 
        }

        return sum;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */