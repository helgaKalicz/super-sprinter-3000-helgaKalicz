from flask import Flask, request, render_template, redirect
import functions
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def listing():
    '''
    Lists all stories from the file.
    '''
    story_list = functions.restore_comma(functions.read_file('result.txt'))
    return render_template('list.html', file_list=story_list)


@app.route('/story', methods=['GET'])
def a_new_story():
    '''
    Allows to fill an empty form out with a story.
    '''
    return render_template('form.html', story=None)


@app.route('/story', methods=['POST'])
def add_new_story():
    '''
    Writes the new story to the file, based on the user inputs.
    '''
    if functions.valid_value(request.form['business_value']) and functions.valid_time(request.form['estimation_time']):
        with open('result.txt', 'a') as file:
            file.write(str(int(functions.read_file('result.txt')[-1][0]) + 1) + ',')
            file.write(str(functions.convert_string(request.form['story_title'])) + ',')
            file.write(str(functions.convert_string(request.form['user_story'])) + ',')
            file.write(str(functions.convert_string(request.form['acceptance_criteria'])) + ',')
            file.write(str(int(request.form['business_value'])) + ',')
            file.write(str(functions.correct_time(request.form['estimation_time'])) + ',')
            file.write(str(request.form['status']) + '\n')
        return redirect('/list')
    else:
        return render_template('error.html')


@app.route('/story/<int:story_id>', methods=['GET'])
def show_story(story_id):
    '''
    Redirects to a page where the user can change the elements of the chosen story.
    '''
    story_list = functions.restore_comma(functions.read_file('result.txt'))
    selected_story = ''
    for story in story_list:
        if int(story[0]) == int(story_id):
            selected_story = story
            break
    return render_template('form.html', story=selected_story, story_id=story_id)


@app.route('/story/<int:story_id>', methods=['POST'])
def modify_story(story_id):
    '''
    Saves the changes to the file, based on the user inputs.
    '''
    if functions.valid_value(request.form['business_value']) and functions.valid_time(request.form['estimation_time']):
        story_list = functions.read_file('result.txt')
        for story in story_list:
            if int(story[0]) == int(story_id):
                story[1] = str(functions.convert_string(request.form['story_title']))
                story[2] = str(functions.convert_string(request.form['user_story']))
                story[3] = str(functions.convert_string(request.form['acceptance_criteria']))
                story[4] = str(int(request.form['business_value']))
                story[5] = str(functions.correct_time(request.form['estimation_time']))
                story[6] = str(request.form['status'])
                break
        functions.write_file('result.txt', story_list)
        return redirect('/list')
    else:
        return render_template('error.html')


@app.route('/story/<int:story_id>/delete', methods=['POST'])
def delete_story(story_id):
    '''
    Deletes the chosen story from the file.
    '''
    story_list = functions.read_file('result.txt')
    for story in story_list:
        if int(story[0]) == int(story_id):
            story_list.remove(story)
    functions.write_file('result.txt', story_list)
    return redirect('/list')


@app.errorhandler(404)
def error_handling(e):
    '''
    Handles errors.
    '''
    return render_template('error.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
