#A to do list program

#import PySimpleGUI as sg


idStart = 1

toDoList = {}

def getInput():
	activity = input("Pls type in an activity")
	return activity

def addToList(activity):
	global toDoList
	toDoList.[start] = activity
	print ("Activity added successfully")

def removeActivity(start):
	global toDoList
	todoList.pop(start)
	print ("Activity successfully removed")

def editToDoList(start):
	newActivity = getInput();
	todoList[start] = newActivity
	print ("Activity successfully edited")


def main():
	pass




