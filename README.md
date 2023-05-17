# Fast API Boilerplate
<p>This is a boilerplate code for a FastAPI application with SQLAlchemy as the database ORM. The application includes a simple endpoint "/api/healthchecker" that returns a JSON response.</p>

<h2>Requirements</h2>
<ul>
<li>Python 3.6+</li>
<li>FastAPI</li>
<li>SQLAlchemy</li>
</ul>

<h2>Installation</h2>
<ol>
<li>Clone the repository: <code>git clone https://github.com/&lt;username&gt;/&lt;repo-name&gt;.git</code></li>
<li>Install dependencies: <code>pip install -r requirements.txt</code></li>
<li>Run the application: <code>python main.py</code></li>
</ol>

<h2>Usage</h2>
<p>Once the application is running, you can access the API endpoints:</p>
<ul>
<li><code>/api/healthchecker</code> - Returns a JSON response indicating the server is up and running</li>
<li><code>/api/notes</code> - CRUD operations for managing notes</li>
</ul>

<h2>CORS Configuration</h2>
<p>The application includes middleware to enable Cross-Origin Resource Sharing (CORS) with the following origins:</p>
<ul>
<li>http://localhost:3000</li>
</ul>
<p>If you want to allow other origins, you can modify the <code>origins</code> list in the <code>main.py</code> file.</p>

<h2>Database Setup</h2>
<p>The application uses SQLAlchemy as the ORM for connecting to the database. To create the necessary tables in your database, run the following command:</p>
<pre><code>from .models import Note
from .database import engine

Note.Base.metadata.create_all(bind=engine)
</code></pre>
<p>You can modify the database connection settings in the <code>database.py</code> file.</p>