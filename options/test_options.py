from .base_options import BaseOptions

class TestOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)

        self.parser.add_argument('--results_dir', type=str, default='gin_places2', help='saves results here')
        self.parser.add_argument('--phase', type=str, default='test', help='train or test')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load?')              

        
        self.parser.add_argument('--pretrained_path', type=str, default='./checkpoints/latest_net_G.pth')
        self.parser.add_argument('--level', type=int, required=True)
        self.parser.add_argument('--split', type=int, default=0)
        self.parser.add_argument('--total', type=str, default=1)

        self.isTrain = False

