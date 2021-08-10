class TimeManager:
    def __init__(self, game_state):
        self.game_state = game_state
        self.elapsed_time = 0
    
    
    def handle_time_passed(self, this_frame_elapsed_time):
        self.elapsed_time = self.elapsed_time + this_frame_elapsed_time
        tpm = self.time_per_move()
        while self.elapsed_time > tpm:
            self.elapsed_time = self.elapsed_time - tpm
            self.game_state.move_snake()
        
    def time_per_move(self):
        ss = self.game_state.snake_speed
        # transform snake speed into time per move
        tpm = 500
        while ss > 1:
            tpm = tpm - tpm*0.1
            ss = ss - 1
        return int(tpm)
    
    