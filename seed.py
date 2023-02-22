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

trek_1 = Trek ("Snowdon Ascent", 14.5, 1, "Reach the summit of Snowdon via Llanberris Path", False, "Parking at Pen-y-Pass is now paid - use park n ride from llanberris. Best to start early to avoid crowds on summit!", destination_1)
trek_repository.save(trek_1)

trek_2 = Trek ("Glyders Traverse", 6.6, 1, "Traverse the Glyders via Tryfan", True, "Starting in the Ogwen Valley and climbing directly up the famous north ridge of Tryfan (a Grade 1 scramble renowned for tricky route-finding), this route is suited to experienced scramblers who are comfortable with rocky and exposed mountain terrain.", destination_1)
trek_repository.save(trek_2)

trek_3 = Trek ("Cairn Gorm & Ben Macdui", 17.5, 1, "Summit Ben Macdui crossing the Cairn Gorm Plateau", False, "A big day out! Very little shelter or escape routes - ensure good weather forecast. No signal for majority of the day - consider GPS beacon?", destination_2)
trek_repository.save(trek_3)



