change = float(input())
change_in_stotinki = int(change * 100)
coin_counter = 0

while change_in_stotinki > 0:
    if change_in_stotinki >= 200:
        coin_counter += change_in_stotinki // 200
        change_in_stotinki = change_in_stotinki % 200
    elif change_in_stotinki >= 100:
        coin_counter += change_in_stotinki // 100
        change_in_stotinki = change_in_stotinki % 100
    elif change_in_stotinki >= 50:
        coin_counter += change_in_stotinki // 50
        change_in_stotinki = change_in_stotinki % 50
    elif change_in_stotinki >= 20:
        coin_counter += change_in_stotinki // 20
        change_in_stotinki = change_in_stotinki % 20
    elif change_in_stotinki >= 10:
        coin_counter += change_in_stotinki // 10
        change_in_stotinki = change_in_stotinki % 10
    elif change_in_stotinki >= 5:
        coin_counter += change_in_stotinki // 5
        change_in_stotinki = change_in_stotinki % 5
    elif change_in_stotinki >= 2:
        coin_counter += change_in_stotinki // 2
        change_in_stotinki = change_in_stotinki % 2
    elif change_in_stotinki >= 1:
        coin_counter += 1
        change_in_stotinki -= 1

print(int(coin_counter))
