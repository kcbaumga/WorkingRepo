using mongodbcarsapi.Models;
using mongodbcarsapi.Services;
using Microsoft.AspNetCore.Mvc;

namespace mongodbcarsapi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class CarsController : ControllerBase
{
     private readonly carsService _CarService;

     public CarsController(carsService CarService) =>
        _CarService = CarService;

    [HttpGet]
    public async Task<List<cardets>> Get() =>
        await _CarService.GetAsync();

    [HttpGet("{id:length(24)}")]
    public async Task<ActionResult<cardets>> Get(string id)
    {
        var car = await _CarService.GetAsync(id);

        if (car is null)
        {
            return NotFound();
        }

        return car;
    }
    [HttpPost]
    public async Task<IActionResult> Post(cardets newCar)
    {
        await _CarService.CreateAsync(newCar);

        return CreatedAtAction(nameof(Get), new { id = newCar.Id }, newCar);
    }
    [HttpPut("{id:length(24)}")]
    public async Task<IActionResult> Update(string id, cardets updatedCar)
    {
        var car = await _CarService.GetAsync(id);

        if (car is null)
        {
            return NotFound();
        }

        updatedCar.Id = car.Id;

        await _CarService.UpdateAsync(id, updatedCar);

        return NoContent();
    }

    [HttpDelete("{id:length(24)}")]
    public async Task<IActionResult> Delete(string id)
    {
        var car = await _CarService.GetAsync(id);

        if (car is null)
        {
            return NotFound();
        }

        await _CarService.RemoveAsync(id);

        return NoContent();
    }

}

