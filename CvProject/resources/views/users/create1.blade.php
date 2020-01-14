<div class="container mt-5">
    @alertt
        @foreach ($errors->all() as $message)
            {{ $message }}
        @endforeach
    @endalertt
    <form method="GET" action="/users/create">
        @csrf
        <div class="form-group">
            <label for="exampleInputEmail1">name</label>
            <input name="name" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>
       

        <div class="form-group form-check">
            <input name="email" type="email" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">email</label>
        </div>

        <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input name="password" type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

</div>