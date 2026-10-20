class NumMatrix {
    int[][] pm;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        this.pm = new int[m][n];

        for (int i = 0; i < m; i++) {
            int prefix = 0;
            for (int j = 0; j < n; j++) {
                prefix += matrix[i][j];
                this.pm[i][j] = prefix + this.pm[Math.max(0, i-1)][j];
                System.out.print("%d ".formatted(this.pm[i][j]));
            }
            System.out.println("");
        }
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res = pm[row2][col2];
        if (col1 > 0) res -= pm[row2][col1-1];
        if (row1 > 0) res -= pm[row1-1][col2];
        if (row1 > 0 && col1 > 0) res += pm[row1-1][col1-1];

        return res;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */