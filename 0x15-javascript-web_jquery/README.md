<!DOCTYPE html>
<html lang="en">

<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

<body>
    <p>Manual QA Review It is your responsibility to request a review for this project from a peer before the project&rsquo;s deadline. If no peers have been reviewed, you should request a review from a TA or staff member. Quiz questions Show Tasks 0. No JQuery mandatory Write a JavaScript script that updates the text color of the</p>
    <header>element to red (#FF0000): You must use document.querySelector to select the HTML tag You can&rsquo;t use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 0-main.html <title>Holberton School</title>
        <header>First HTML page</header>
        <footer>Holberton School - 2017</footer>
        <script type="text/javascript" src="0-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 0-script.js 1. With JQuery mandatory Write a JavaScript script that updates the text color of the<header>element to red (#FF0000): You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 1-main.html <title>Holberton School</title>
            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
            <header>First HTML page</header>
            <footer>Holberton School - 2017</footer>
            <script type="text/javascript" src="1-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 1-script.js 2. Click and turn red mandatory Write a JavaScript script that updates the text color of the<header>element to red (#FF0000) when the user clicks on the tag DIV#red_header: You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 2-main.html <title>Holberton School</title>
                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                <header>First HTML page</header>
                <div id="red_header">Red header</div>
                <footer>Holberton School - 2017</footer>
                <script type="text/javascript" src="2-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 2-script.js 3. Add `.red` class mandatory Write a JavaScript script that adds the class red to the<header>element when the user clicks on the tag DIV#red_header You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 3-main.html <title>Holberton School</title>
                    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                    <style>
                        .red {
                            color: #FF0000;
                        }
                    </style>
                    <header>First HTML page</header>
                    <div id="red_header">Red header</div>
                    <footer>Holberton School - 2017</footer>
                    <script type="text/javascript" src="3-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 3-script.js 4. Toggle classes mandatory Write a JavaScript script that toggles the class of the<header>element when the user clicks on the tag DIV#toggle_header: The<header>element must always have one class: red or green, never both in the same time and never empty. If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse. You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 4-main.html <title>Holberton School</title>
                            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                            <style>
                                .red {
                                    color: #FF0000;
                                }

                                .green {
                                    color: #00FF00;
                                }
                            </style>
                            <header class="green">First HTML page</header>
                            <div id="toggle_header">Toggle header</div>
                            <footer>Holberton School - 2017</footer>
                            <script type="text/javascript" src="4-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 4-script.js 5. List of elements mandatory Write a JavaScript script that adds a<ul>
                                <li>element to a list when the user clicks on the tag DIV#add_item: The new element must be:</li>
                                <li>Item</li>
                            </ul>The new element must be added to UL.my_list You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 5-main.html <title>Holberton School</title>
                            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                            <header>First HTML page</header><br>
                            <div id="add_item">Add item</div><br>
                            <ul class="my_list">
                                <li>Item</li>
                            </ul>
                            <footer>Holberton School - 2017</footer>
                            <script type="text/javascript" src="5-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 5-script.js 6. Change the text mandatory Write a JavaScript script that updates the text of the<header>element to New Header!!! when the user clicks on DIV#update_header You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 6-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <header>First HTML page</header><br>
                                <div id="update_header">Update the header</div><br>
                                <footer>Holberton School - 2017</footer>
                                <script type="text/javascript" src="6-script.js"></script> guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 6-script.js 7. Star wars character mandatory Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json The name must be displayed in the HTML tag DIV#character You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 7-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <header>Star Wars character</header><br>
                                <div id="character"><br></div><br>
                                <footer>Holberton School - 2017</footer>
                                <script type="text/javascript" src="7-script.js"></script> guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 7-script.js 8. Star Wars movies mandatory Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json All movie titles must be list in the HTML tag UL#list_movies You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 8-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <header>Star Wars movies</header><br><br>
                                <footer>Holberton School - 2017</footer>
                                <script type="text/javascript" src="8-script.js"></script> guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 8-script.js 9. Say Hello! mandatory Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello. The translation of &ldquo;hello&rdquo; must be displayed in the HTML tag DIV#hello You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Your script must work when it is imported from the tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 9-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <script type="text/javascript" src="9-script.js"></script>
                                <header>Say Hello!</header><br>
                                <div id="hello"><br></div><br>
                                <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 9-script.js 10. No jQuery - document loaded #advanced Write a JavaScript script that updates the text color of the<header>element to red (#FF0000): You must use document.querySelector to select the HTML tag You can&rsquo;t use the jQuery API Note: Your script must be imported from the tag, not at the end of the HTML Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 100-main.html <title>Holberton School</title>
                                    <script type="text/javascript" src="100-script.js"></script>
                                    <header>First HTML page</header>
                                    <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 100-script.js 11. List, add, remove #advanced Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks: The new element must be:<ul>
                                        <li>Item</li>
                                    </ul>The new element must be added to UL.my_list When the user clicks on DIV#add_item: a new element is added to the list When the user clicks on DIV#remove_item: the last element is removed from the list When the user clicks on DIV#clear_list: all elements of the list are removed You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API You script must work when it imported from the HEAD tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 101-main.html <title>Holberton School</title>
                                    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                    <script type="text/javascript" src="101-script.js"></script>
                                    <header>First HTML page</header><br>
                                    <div id="add_item">Add item</div>
                                    <div id="remove_item">Remove item</div>
                                    <div id="clear_list">Clear list</div><br>
                                    <ul class="my_list">
                                        <li>Item</li>
                                    </ul>
                                    <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 101-script.js 12. Say hello to everybody! #advanced Write a JavaScript script that fetches and prints how to say &ldquo;Hello&rdquo; depending on the language You should use this API service: https://www.fourtonfish.com/hellosalut/hello/ The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.) The translation must be fetched when the user clicks on INPUT#btn_translate The translation of &ldquo;Hello&rdquo; must be displayed in the HTML tag DIV#hello You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API You script must work when imported from the tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 102-main.html <title>Holberton School</title>
                                    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                    <script type="text/javascript" src="102-script.js"></script>
                                    <header>Say Hello</header><br><input id="language_code" type="text" placeholder="Language code">&nbsp;<input id="btn_translate" type="button" value="Translate"><br>
                                    <div id="hello"><br></div><br>
                                    <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 102-script.js 13. And press ENTER #advanced Write a JavaScript script that fetches and prints how to say &ldquo;Hello&rdquo; depending on the language You should use this API service: https://www.fourtonfish.com/hellosalut/hello/ The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.) The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code The translation of &ldquo;Hello&rdquo; must be displayed in the HTML tag DIV#hello You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API You script must work when imported from the tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 103-main.html <title>Holberton School</title>
                                    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                    <script type="text/javascript" src="103-script.js"></script>
                                </header>
                            </header>
                        </header>
                    </header>
                </header>
            </header>
        </header>
    </header>
    <header>First HTML page</header>
    <footer>Holberton School - 2017</footer>
    <script type="text/javascript" src="0-script.js"></script>
    <p>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 0-script.js 1. With JQuery mandatory Write a JavaScript script that updates the text color of the</p>
    <header>element to red (#FF0000): You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 1-main.html <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <header>First HTML page</header>
        <footer>Holberton School - 2017</footer>
        <script type="text/javascript" src="1-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 1-script.js 2. Click and turn red mandatory Write a JavaScript script that updates the text color of the<header>element to red (#FF0000) when the user clicks on the tag DIV#red_header: You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 2-main.html <title>Holberton School</title>
            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
            <header>First HTML page</header>
            <div id="red_header">Red header</div>
            <footer>Holberton School - 2017</footer>
            <script type="text/javascript" src="2-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 2-script.js 3. Add `.red` class mandatory Write a JavaScript script that adds the class red to the<header>element when the user clicks on the tag DIV#red_header You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 3-main.html <title>Holberton School</title>
                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                <style>
                    .red {
                        color: #FF0000;
                    }
                </style>
                <header>First HTML page</header>
                <div id="red_header">Red header</div>
                <footer>Holberton School - 2017</footer>
                <script type="text/javascript" src="3-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 3-script.js 4. Toggle classes mandatory Write a JavaScript script that toggles the class of the<header>element when the user clicks on the tag DIV#toggle_header: The<header>element must always have one class: red or green, never both in the same time and never empty. If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse. You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 4-main.html <title>Holberton School</title>
                        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                        <style>
                            .red {
                                color: #FF0000;
                            }

                            .green {
                                color: #00FF00;
                            }
                        </style>
                        <header class="green">First HTML page</header>
                        <div id="toggle_header">Toggle header</div>
                        <footer>Holberton School - 2017</footer>
                        <script type="text/javascript" src="4-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 4-script.js 5. List of elements mandatory Write a JavaScript script that adds a<ul>
                            <li>element to a list when the user clicks on the tag DIV#add_item: The new element must be:</li>
                            <li>Item</li>
                        </ul>The new element must be added to UL.my_list You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 5-main.html <title>Holberton School</title>
                        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                        <header>First HTML page</header><br>
                        <div id="add_item">Add item</div><br>
                        <ul class="my_list">
                            <li>Item</li>
                        </ul>
                        <footer>Holberton School - 2017</footer>
                        <script type="text/javascript" src="5-script.js"></script>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 5-script.js 6. Change the text mandatory Write a JavaScript script that updates the text of the<header>element to New Header!!! when the user clicks on DIV#update_header You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 6-main.html <title>Holberton School</title>
                            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                            <header>First HTML page</header><br>
                            <div id="update_header">Update the header</div><br>
                            <footer>Holberton School - 2017</footer>
                            <script type="text/javascript" src="6-script.js"></script> guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 6-script.js 7. Star wars character mandatory Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json The name must be displayed in the HTML tag DIV#character You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 7-main.html <title>Holberton School</title>
                            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                            <header>Star Wars character</header><br>
                            <div id="character"><br></div><br>
                            <footer>Holberton School - 2017</footer>
                            <script type="text/javascript" src="7-script.js"></script> guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 7-script.js 8. Star Wars movies mandatory Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json All movie titles must be list in the HTML tag UL#list_movies You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 8-main.html <title>Holberton School</title>
                            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                            <header>Star Wars movies</header><br><br>
                            <footer>Holberton School - 2017</footer>
                            <script type="text/javascript" src="8-script.js"></script> guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 8-script.js 9. Say Hello! mandatory Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello. The translation of &ldquo;hello&rdquo; must be displayed in the HTML tag DIV#hello You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API Your script must work when it is imported from the tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 9-main.html <title>Holberton School</title>
                            <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                            <script type="text/javascript" src="9-script.js"></script>
                            <header>Say Hello!</header><br>
                            <div id="hello"><br></div><br>
                            <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 9-script.js 10. No jQuery - document loaded #advanced Write a JavaScript script that updates the text color of the<header>element to red (#FF0000): You must use document.querySelector to select the HTML tag You can&rsquo;t use the jQuery API Note: Your script must be imported from the tag, not at the end of the HTML Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 100-main.html <title>Holberton School</title>
                                <script type="text/javascript" src="100-script.js"></script>
                                <header>First HTML page</header>
                                <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 100-script.js 11. List, add, remove #advanced Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks: The new element must be:<ul>
                                    <li>Item</li>
                                </ul>The new element must be added to UL.my_list When the user clicks on DIV#add_item: a new element is added to the list When the user clicks on DIV#remove_item: the last element is removed from the list When the user clicks on DIV#clear_list: all elements of the list are removed You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API You script must work when it imported from the HEAD tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 101-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <script type="text/javascript" src="101-script.js"></script>
                                <header>First HTML page</header><br>
                                <div id="add_item">Add item</div>
                                <div id="remove_item">Remove item</div>
                                <div id="clear_list">Clear list</div><br>
                                <ul class="my_list">
                                    <li>Item</li>
                                </ul>
                                <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 101-script.js 12. Say hello to everybody! #advanced Write a JavaScript script that fetches and prints how to say &ldquo;Hello&rdquo; depending on the language You should use this API service: https://www.fourtonfish.com/hellosalut/hello/ The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.) The translation must be fetched when the user clicks on INPUT#btn_translate The translation of &ldquo;Hello&rdquo; must be displayed in the HTML tag DIV#hello You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API You script must work when imported from the tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 102-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <script type="text/javascript" src="102-script.js"></script>
                                <header>Say Hello</header><br><input id="language_code" type="text" placeholder="Language code">&nbsp;<input id="btn_translate" type="button" value="Translate"><br>
                                <div id="hello"><br></div><br>
                                <footer>Holberton School - 2017</footer>guillaume@ubuntu:~/0x15$ Repo: GitHub repository: holbertonschool-higher_level_programming Directory: 0x15-javascript-web_jquery File: 102-script.js 13. And press ENTER #advanced Write a JavaScript script that fetches and prints how to say &ldquo;Hello&rdquo; depending on the language You should use this API service: https://www.fourtonfish.com/hellosalut/hello/ The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.) The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code The translation of &ldquo;Hello&rdquo; must be displayed in the HTML tag DIV#hello You can&rsquo;t use document.querySelector to select the HTML tag You must use the JQuery API You script must work when imported from the tag Please test with this HTML file in your browser: guillaume@ubuntu:~/0x15$ cat 103-main.html <title>Holberton School</title>
                                <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
                                <script type="text/javascript" src="103-script.js"></script>
                                <header>Say Hello</header><br><input id="language_code" type="text" placeholder="Language code">&nbsp;<input id="btn_translate" type="button" value="Translate"><br>
                                <div id="hello"><br></div><br>
                                <footer>Holberton School - 2017</footer>
                            </header>
                        </header>
                    </header>
                </header>
            </header>
        </header>
    </header>
</body>

</html>