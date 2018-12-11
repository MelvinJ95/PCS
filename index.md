# **PCS - Personal Cashier System** # 

## Brief Overlook ## 

#### PCS (or Personal Cashier System) is a resulting programming language from the necessity to help independent merchants and mobile salesmen to set up their own store without having to rely upon third-party companies or freelance developers. Most mobile stores exist independent from a company that would normally grant them funds to sustain and build their store. These, on the other hand, depend solely on the respective store owner's budget. It is preferrable that they do not have to spend some of their limited resources to have to be able to set up their store. Despite having the alternative of utilizing pre-existing methods such as traditional cash registers, ATMs, and/or mobile money transferring, PCS pretends to facilitate and bring new flavor to their service by offering a more modern and convenient system, which can be used in unison with the previously method alternatives. #### 
{: style="text-align: justify"}

#### With the upcoming times, an array of fast foods are replacing cashiers with tablet-like systems that provide a simple UI for customers to see what the store has to offer, with images, descriptions and respective prices. These also provide clients the ability to self-service themselves, and make the complete order in the aforementioned system. PCS wants to follow the same dynamic, being able to provide that respective experience, but for smaller businesses in mind. ####
{: style="text-align: justify"}

#### Preliminarily, PCS will intend to provide a basic, yet customizable GUI layout containing the name of the respective service, and two containers: one for the store's content with image, descriptions and prices, and another tallying up the total of the purchase as items from the store that are being selected for purchase. Last, but not least, it will provide a customizable receipt layout, which acts as a validation of purchase to the respective store. #####
{: style="text-align: justify"}

## Basic Language Syntax and Operations ##

#### Below will be a set of examples for basic functionalities that PCS provides to the user. #####

### **Create the shop** ###
'''
      view shop
'''
#### Command creates basic GUI layout and later on allows to visualize the current state of the store.  ####

### **Change store name** ###
'''
      view set_shop_name desired_name
'''

#### Command allows user to change store or service named to the one specified as input.  ####

### **Add elements to the shop** ###
'''
      view add_item icon, name, type, price
'''

#### Commands allows user to add a respective element to the store. Creates an icon and locks it into the store's inventory's container with the selected image and name.  ####

### **Edit receipt elements** ###
'''
      receipt append desired_name to header/footer
'''

#### Command allows user to alter the header or footer of the receipt to the desired content desired.  ####
## Video Demonstration ## 

<html> <body> <iframe width="560" height="315" src="https://www.youtube.com/embed/9LT2g4jJGm8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> </body> </html>

## Future Work ## 

For further implementations, PCS wants to provide more customization and functionalities. 

**Future Implementation** | **Description**
------------- | -------------
**Real-time Modifications**  | The user will be able to add elements to store, reflect items from database, and customize layout in realtime. 
**Database Implementation**  | A database will be added to organize store inventory in a more organized manner, plus monitor sales.  
**Sales Report Management** | A report view will be implemented that will allow the store owner to generate sale reports within a specific timeframe and be able to see what items were sold during said period, or filter to view sales per item type and see purchase behavior within the store.
**More Customization Alternatives** | New pre-designed themes are planned to be added, alongside with the alternative to take themes and tweak colored elements and positioning of GUI elements, and allow for respective container resizing.

{: style="text-align: justify"}
