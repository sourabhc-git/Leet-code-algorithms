class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        int n = mat.length;
        for(int rotation = 0; rotation < 4; rotation++){
            if(isMatricsEqual(mat, target)){
                return true;
            }
            mat = rotated(mat, n);
        }
        return false;
    }

    boolean isMatricsEqual(int[][] mat, int[][] target){

      int n = mat.length;
      for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if (mat[i][j] != target[i][j]){
                return false;
            }
        }
      }
        return true;
    }

    int[][] rotated(int[][] mat, int n){
        int[][] rotated = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
            
           
            rotated[j][n - 1 - i] = mat[i][j];

        }
        
        }
        return rotated;
       
    }
}