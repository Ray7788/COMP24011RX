import java.util.ArrayList;  

public class MoveChooser {
	// this class is designed for computer player
    // numbers reflect the value for a player of being on the respective square
    public static int positionValue[][] = {   
        {120, -20, 20, 5, 5, 20, -20, 120},
        {-20, -40, -5, -5, -5, -5, -40, -20},
        {20, -5, 15, 3, 3, 15, -5, 20},
        {5, -5, 3, 3, 3, 3, -5, 5},
        {5, -5, 3, 3, 3, 3, -5, 5},
        {20, -5, 15, 3, 3, 15, -5, 20},
        {-20, -40, -5, -5, -5, -5, -40, -20},
        {120, -20, 20, 5, 5, 20, -20, 120},
    };

    public static Move chooseMove(BoardState boardState){


        ArrayList<Move> moves= boardState.getLegalMoves();
        if(moves.isEmpty()){
            return null;
		}
        // return moves.get(0);
        return topLevel(boardState, moves);
    }


    /////////////////////////////////////////////////  write a better move selection function ///////////////////////////////////////

    // board position = + weights of all those squares occupied by white pieces - weights of those squares occupied by black pieces.
    public static int staticEvaluation(BoardState boardState){
    	int weight = 0;
    	for(int i=0; i<8; i++){
    		for(int j=0; j<8; j++){
                // white
    			if(boardState.getContents(i, j)== 1){
    				weight += positionValue[i][j]; 
                // black
    			}else if(boardState.getContents(i,j)== -1){
    				weight -= positionValue[i][j];
    			}
    		}
    	}
    		return weight;
    } 

    // αβ-pruning DFS
    public static int miniMax(BoardState boardState, int searchDepth, int alpha, int beta, Boolean maxmizingNode){
    	ArrayList<Move> move = boardState.getLegalMoves();
		//
    	if(searchDepth==0){
    		return staticEvaluation(boardState);
    	}else if(maxmizingNode){
    		alpha = Integer.MIN_VALUE;  // lower bound

    		for(int i = 0 ; i<move.size(); i++){
    			if(alpha >= beta||move.isEmpty()){
    				break;
    			}
                // a fresh copy of boardState
    			BoardState boardState1 = boardState.deepCopy();
    			boardState1.makeLegalMove(move.get(i).x, move.get(i).y);
    			int miniVal = miniMax(boardState1, searchDepth-1, alpha, beta, false);	// next is minimizing
    			if(alpha < miniVal){	// update alpha
    				alpha = miniVal;	
    			}
    		}
    		return alpha;
    	}else{
    		beta = Integer.MAX_VALUE;   // upper bound

    		for(int i = 0; i<move.size(); i++){
    			if(alpha >= beta||move.isEmpty()){
    				break;
    			}
                // a fresh copy of boardState
    			BoardState boardState1 = boardState.deepCopy();
    			boardState1.makeLegalMove(move.get(i).x, move.get(i).y);
    			int maxVal = miniMax(boardState1, searchDepth-1, alpha, beta, true);	// next is maxmizing
    			if(maxVal < beta){		// update beta
    				beta = maxVal;
    			}
    		}
    		return beta;
    	}
    }

    // The top-level call
    public static Move topLevel(BoardState bs, ArrayList<Move> move){
        int searchDepth= Othello.searchDepth;
    	int valueIndex = 0;
    	int a = Integer.MIN_VALUE;	// negative infinity
    	int b = Integer.MAX_VALUE;	// positive infinity
    	Move bestChoice = null;	// set when there are no moves available as the default value 

    	for(int i=0; i<move.size(); i++){
    		BoardState temp = bs.deepCopy();
    		temp.makeLegalMove(move.get(i).x, move.get(i).y);
    		int minimax = miniMax(temp, searchDepth-1, a, b, false);	// at the beginning set to minimizing node
    		if(a<minimax){
    			a=minimax;
    			valueIndex = i;
    		}
    	}

    	bestChoice = move.get(valueIndex);
    	return bestChoice;
    }
 
}
