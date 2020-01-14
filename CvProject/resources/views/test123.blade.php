
@extends('layouts.app')
<div class="container mt-5">
<h1>Plantilla CV</h1>

<h3 class="titulos">Datos personales (profile)</h3>

<h4>{{$profile[0]->Nombre}} {{$profile[0]->Apellidos}}</h4>
<h4>{{$profile[0]->Intro}}</h4>
<h4>{{$profile[0]->Correo}}</h4>


<h3 class="titulos">Empleo (job)</h3>
<h4>{{$jobs[0]->empleo}}</h4>
<h3 class="titulos">Educación (education)</h3>
<h4>{{$education[0]->Formacion}}</h4>
<h3 class="titulos">Habilidad (hability)</h3>


@foreach($hability as $key => $hability1)
   <h4> {{$hability1->habilidad}}</h4>
@endforeach

<h3 class="titulos">Hobbie (hobbie)</h3>
<h4>{{$hobbie[0]->nombre}}</h4>




</div>








<style>
    .titulos{
        color:red
    }
</style>



