// juego.test.js
const { verificarIntento, calcularPuntaje } = require('./juego');
 
// ── verificarIntento ──────────────────────────────────────
 
test('intento correcto', () => {
    expect(verificarIntento(42, 42)).toBe("correcto");
});
 
test('intento es muy bajo, pista dice mayor', () => {
    expect(verificarIntento(48, 5)).toBe("mayor");  // completar
});
 
test('intento es muy alto, pista dice menor', () => {
    expect(verificarIntento(72, 92)).toBe("menor");  // completar
});
 
test('intento fuera de rango lanza excepción', () => {
    expect(() => verificarIntento(50, 120)).toThrow("El número debe estar entre 1 y 100");
});
 
test('intento no numérico lanza excepción', () => {
    expect(() => verificarIntento(50, "a")).toThrow("El intento debe ser un número");
});
 
// ── calcularPuntaje ───────────────────────────────────────
 
test('3 intentos o menos dan puntaje 100', () => {
    expect(calcularPuntaje(2)).toBe(100);  // completar
    expect(calcularPuntaje(3)).toBe(100);
});
 
test('entre 4 y 6 intentos dan puntaje 75', () => {
    expect(calcularPuntaje(4)).toBe(75);
    expect(calcularPuntaje(5)).toBe(75);
});
 
test('entre 7 y 10 intentos dan puntaje 50', () => {
    expect(calcularPuntaje(7)).toBe(50);
    expect(calcularPuntaje(8)).toBe(50);
    expect(calcularPuntaje(9)).toBe(50);
});
 
test('más de 10 intentos dan puntaje 25', () => {
    expect(calcularPuntaje(11)).toBe(25);
});
