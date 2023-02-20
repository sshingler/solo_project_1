import pdb
from models.trek import Trek
from models.destination import Destination 

import repositories.trek_repository as trek_repository 
import repositories.destination_repository as destination_repository 

trek_repository.delete_all()
destination_repository.delete_all()

destination_1 = Destination("Snowdonia National Park", "United Kingdom", "Europe")
destination_repository.save(destination_1)

destination_2 = Destination("Cairn Gorms National Park", "United Kingdom", "Europe")
destination_repository.save(destination_2)

trek_1 = Trek ("Snowdon Ascent", 14.5, 1, "Reach the summit of Snowdon via Llanberris Path", False, "Test notes 123", destination_1)
trek_repository.save(trek_1)

trek_2 = Trek ("Glyders Traverse", 6.6, 1, "Traverse the Glyders via Tryfan", True, "Test notes 123", destination_1)
trek_repository.save(trek_2)

trek_3 = Trek ("Cairn Gorm & Ben Macdui", 17.5, 1, "Summit Ben Macdui crossing the Cairn Gorm Plateau", False, "Test notes 123", destination_2)
trek_repository.save(trek_3)
