# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        #create a new updater object to handle the item updates
        updater = qualityUpdater()
        
        #create a list of legendary names to make the legendary item specification scalable easier, added some other WoW legendaries for fun :)
        legendaries = ['Sulfuras, Hand of Ragnaros', 'Thunderfury, Blessed Blade of the Windseeker', 'Atiesh, Greatstaff of the Guardian']
        
        #call each specific type of updater dependant on the logic in requirements
        for item in self.items:
            if item.name == 'Aged Brie':
                updater.brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                updater.passes(item)
            elif item.name in legendaries:
                updater.legendary(item)
            elif 'Conjured' in item.name:
                updater.conjured(item)
            else:
                updater.normal(item)
                
#OLD CODE BELOW
""" def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
"""

#creating a new class to handle most of the logic needed when updating items, also allows adding new item types easier
class qualityUpdater(object):
    #setting the global max and min qual values detailed in the reqs
    min_quality = 0
    max_quality = 50
    
    #function for normal items
    def normal(self, item):
        if item.sell_in > 0:
            degrades = -1
        else:
            degrades = -2 
        item.quality = max((item.quality + degrades), self.min_quality)
        item.sell_in = item.sell_in-1
    
    #function for brie
    def brie(self, item):
        if item.sell_in > 0:
            degrades = 1
        else:
            degrades = 2
        item.quality = min((item.quality + degrades), self.max_quality)
        item.sell_in = item.sell_in-1

    #function for conjured items
    def conjured(self, item):
        if item.sell_in > 0:
            degrades = -2
        else:
            degrades =-4
        
        item.quality = max((item.quality + degrades), self.min_quality)
        item.sell_in = item.sell_in-1
    
    #function for passes
    def passes(self, item):
        #create a function to avoid code duplication (cheated for this a little as I saw it online when doing my inital look around)
        def set_pass_qual(item, degrades):
            item.quality = min(item.quality + degrades, self.max_quality)
            
        if item.sell_in > 10:
            degrades = 1
            set_pass_qual(item, degrades)
        elif item.sell_in > 5:
            degrades = 2
            set_pass_qual(item, degrades)
        elif item.sell_in > 0:
            degrades = 3
            set_pass_qual(item, degrades)
        else:
            item.quality = 0
        item.sell_in = item.sell_in-1
            
    #function for legendary items    
    def legendary(self, item):
        #nothing needs changed for legendary items so we just pass this section
        #could also use this to check legendaries have the correct value set by making it always set qual to 80, didn't think it was needed for this exercise
        pass
    
    

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
