import pdb
from models.trek import Trek
from models.destination import Destination 

import repositories.trek_repository as trek_repository 
import repositories.destination_repository as destination_repository 

trek_repository.delete_all()
destination_repository.delete_all()

destination_1 = Destination("Snowdonia National Park", "United Kingdom", "Europe")
destination_repository.save(destination_1)

destination_2 = Destination("Cairngorms National Park", "United Kingdom", "Europe")
destination_repository.save(destination_2)

trek_1 = Trek ("Snowdon Ascent", 14.5, 1, "Reach the summit of Snowdon via Llanberris Path", False, "Test notes 123", destination_1)
trek_repository.save(trek_1)

trek_2 = Trek ("Glyders Traverse", 6.6, 1, "Traverse the Glyders via Tryfan", True, "Starting in the Ogwen Valley and climbing directly up the famous north ridge of Tryfan (a Grade 1 scramble renowned for tricky route-finding), this route is suited to experienced scramblers who are comfortable with rocky and exposed mountain terrain. There are easier routes up Tryfan but all require the use of hands in some places, so not ideal for inexperienced walkers. From Tryfan you follow a steep path to the otherworldly summits of Glyder Fach and Glyder Fawr, with their spectacular spiky rocks making you feel like you’ve been transported to some faraway moonscape. On a clear day you’ll be rewarded with magical views across to Snowdon – the highest mountain in Wales. The descent via Devil’s Kitchen is rocky and steep, with great views down the Cwm Idwal National Nature Reserve, and the stroll along the eastern edge of Llyn Idwal is a wonderful way to complete the walk.", destination_1)
trek_repository.save(trek_2)

trek_3 = Trek ("Cairn Gorm & Ben Macdui", 17.5, 1, "Summit Ben Macdui crossing the Cairn Gorm Plateau", False, "Test notes 123", destination_2)
trek_repository.save(trek_3)



test_uncompleted_treks = trek_repository.select_uncompleted()

breakpoint()

