from Master import NLP, Visualize, ImageProcessing
import os

# Helper Functions

def process_input_text_query(input_string):
    ob = NLP()
    ob.input_query(input_string)
    tensor = ob.processing()
    #print(tensor)
    output_list = generic_process(tensor, input_string)
    output_ques = input_string.split("and")
    output_ques = '|'.join(output_ques)
    output_list.insert(0, output_ques)
    return output_list

def process_input_image_query(path):
    ob = ImageProcessing()
    obj = Visualize()
    tensor = ob.image_process(path)
    output_string = obj.image_movie(tensor)          # Contains string, image saved path
    output_list = ['Location of image:' + str(path), output_string, 'None', 'None']
    return output_list
    
def generic_process(tensor, input_string):
    obj = Visualize()
    count = tensor[0]
    for i in range(1, tensor[0]+1):
        if i == 1:
            output_string = ''
            output_loc = ''
            output_desc = ''
        else:
            output_string += '|'
            output_loc += '|'
            output_desc += '|'
            
        if tensor[i]=="role":
            output_string += obj.lead_role(tensor[i + count])
            output_loc += 'None'
            output_desc += 'None'
            
        elif tensor[i]=="characters":
            output_string += obj.characters(tensor[i+count])
            output_loc += 'None'
            output_desc += 'None'
        
        elif tensor[i]=="attitude":
            output_string += obj.character(tensor[i+count], tensor[i+count+1])
            count += 1
            output_loc += 'None'
            output_desc += 'None'
            
        elif tensor[i]=="plot":
            output_string += obj.plot(tensor[i+count])
            output_loc += 'None'
            output_desc += 'None'
        
        elif tensor[i]=="appearances":
            output_string += obj.appearances(tensor[i+count], tensor[i+count+1])
            count += 1
            output_loc += 'None'
            output_desc += 'None'
            
        elif tensor[i]=="year":
            output_string += obj.year(tensor[i+count])
            output_loc += 'None'
            output_desc += 'None'
            
        elif tensor[i]=="songs":
            output_string += obj.songs(tensor[i+count])
            output_loc += 'None'
            output_desc += 'None'
        
        elif tensor[i]=="emotion":
            try:
                if ("average" in input_string):
                    (out, loc) = obj.average_emotion(tensor[i+count], 0)
                    output_desc += out
                    output_loc += str(os.getcwd()) + '/' + loc
                    output_string += "None"
                    break
                elif("predict" in ob.temp):
                    output_string += obj.predict()
                    break
            except IndexError as e:
                output_string += "Not enough parameters"
                break
        
        elif tensor[i]=="genre":
            output_string += obj.genre(tensor[i+count])
            output_loc += 'None'
            output_desc += 'None'
            
        elif tensor[i]=="length":
            output_string += obj.length_of_movie(tensor[i+count])
            output_loc += 'None'
            output_desc += 'None'

        elif tensor[i]=="variation":
            (out, loc) = obj.trends(True)
            output_desc += out
            output_loc += str(os.getcwd()) + '/' + loc
            output_string += "None"

        else:
            output_string += "Query does not contain enough parameters."
            
    return [output_string, output_loc, output_desc]
    