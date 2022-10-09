Lab1
================================
### 编写一个Java程序来玩反转录游戏，有时它的商标名称是“奥赛罗”。Reversi是 在一个8 * 8的棋盘上玩的。一般棋子双面为黑白两色，故称“黑白棋”；因为行棋之时将对方棋子翻转，变为己方棋子，故又称“翻转棋”（Reversi）。
---------------------------
在下面的描述中，线段是形成一条连续的直线（水平、垂直或对角线）。  
玩家放置棋子的规则是 ： 棋子必须放置在一个空的正块上，这样就有一条线段穿过放上的棋子，然后通过一个或多个相反颜色的棋子，并以玩家自己的颜色结束。  
当且仅当一个玩家不能移动，但他的对手可以移动时，他才算错过这个回合。 
人类玩家（总是黑色）与计算机（总是白色）。   
点击不代表合法动作的方块只会产生恼人的哔哔声；如果轮到你（玩家：人类）下棋，但你没有合法的移动 ，那么你必须点击棋盘上的任何地方，允许游戏传递到电脑；  
如果你想玩另一个游戏，你需要关闭窗口，重新运行程序。  
此外，最好在电脑“思考”时不要点击。  
最后，作为一种特别的刺激，如果游戏 以电脑的移动而结束，那么你必须点击棋盘才能看到结果。
************************************
### 类文件，配置具体介绍
#### 玩家端（人类）
* 主要的游戏逻辑是在 BoardState 中。
* 数字代表颜色（1表示白色；-1表示黑色，0代表没有）
* getContents(int x, int y)  和  void setContents(int x, int y, int piece)    允许在棋盘方块上检索和设置。
* boolean checkLegalMove(int x, int y),  它检查当 前玩家是否有可能在正方形（x，y）上移动。
* 检索当前玩家的合法移动列表的 方法是ArrayList<Move> getLegalMoves()。 
************************************
  
#### 机器端（电脑）
  * 计算机端（电脑）位于MoveChooser.java 中， 其中的 main 程序创建了一个实例。
  * 这个类所做的唯一 的事情是实现静态方法 chooseMove(BoardState boardState) 在它的当前版本中，这个方法只是获取合法的移动，如果该列表为空，则返回null（记住我说的有时没有 合法的移动），否则返回该列表中的第一个移动。
  * **你所要做的就是 写一个更好的移动选择函数，而不是仅仅选择第一个。**  使用minimax with αβ-pruning
  * searchDepth 设置成8
  * 这些数字反映了一个玩家在各自的方块上的价值。请注意，边缘上的正方形具有很高的值（因为这里的块很难取），而角落上的正方形具有更高的值（因为这里不能取块）。相比之下，相邻的方块有负值，因为这里的一块将允许对手移动到一个高值的方块上。然后，板位置的值可以通过将白块占据的所有方块的权重加起来，然后减去黑块占据的所有方块的权重来定义。
  * 
  
************************************
### 三件事： 
#### static evaluation function
####  calculate minimax values of board positions
#### The top-level call: you have to select the movethat yields the best daughter (from the point of view of the computer player), rather than simply evaluating the daughter