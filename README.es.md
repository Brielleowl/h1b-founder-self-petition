# h1b-founder-self-petition

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Español** · [हिन्दी](README.hi.md)

Una *skill* de IA para fundadores de startups que presentan su propia petición H-1B como **beneficiary-owner**: la empresa de la que posees la mayoría es el peticionario, tú eres el beneficiario, y presentas la petición desde la cuenta en línea de USCIS de la empresa, sin abogado.

Nace de un caso real: una fundadora en solitario, propietaria del 100 % y única directora de una C-corp de Delaware con pocas semanas de vida, presentó una petición de cambio de empleador + extensión para un puesto especializado a tiempo parcial, pagó premium processing y fue aprobada en 11 días hábiles sin RFE. Cada decisión que se debatió, cada campo que se rellenó mal la primera vez y cada documento del paquete están aquí.

## Inicio rápido (sin conocimientos técnicos)

**Con Claude**
1. Descarga `h1b-founder-self-petition.skill` desde los Releases de este repositorio (un solo archivo).
2. Abre Claude → Settings → Capabilities → Skills → Upload y elige ese archivo.
3. Abre un chat nuevo y escribe: **Quiero que mi propia empresa patrocine mi H-1B. Guíame desde el principio.**

Primero hace ocho preguntas sobre tu situación y luego te pide que arrastres al chat los documentos de la empresa y de inmigración. Cuando toque rellenar el formulario, instala la extensión **Claude in Chrome** desde la Chrome Web Store, inicia sesión en la cuenta de USCIS de la empresa y di «rellena el I-129». Rellena el formulario, sube las pruebas y se detiene; tú pagas y pulsas Submit.

**Con ChatGPT**
Abre el enlace del Custom GPT publicado por el mantenedor (ver notas del Release). ChatGPT no puede manejar tu navegador, así que te dice página por página qué escribir.

Los scripts de `scripts/` son para que los ejecute la IA. Tú nunca tienes que ejecutar nada.

## Qué hace

1. **Filtro inicial** — ocho preguntas de opción múltiple: estatus, empresa, participación, LCA, historial de cap, jornada, premium processing, cuenta de USCIS. Te redirige si falta algo.
2. **Lectura de documentos** — acta de constitución, carta del EIN, tabla de capitalización, saldo bancario, contrato de alquiler, pasaporte, I-797, I-94, nóminas, títulos, LCA certificada; construye un único `case.json`.
3. **Preguntas** — solo lo que los documentos no responden (fechas, reparto de horas, redacción del requisito de titulación, cargo del firmante, qué omitir, plan de financiación).
4. **Borradores** — genera desde plantillas la carta de apoyo, la descripción del puesto, la carta de oferta, el contrato laboral, la resolución del consejo y los textos libres del I-129; da un esquema de plan de negocio.
5. **Revisión de coherencia** — lista de todo lo que debe coincidir entre documentos y formulario.
6. **Relleno del formulario** — guía Claude in Chrome por el I-129 y el I-907 en línea, sube las pruebas y coteja el PDF borrador con `case.json`.
7. **Se detiene** antes del pago. Pagas desde la cuenta de la empresa y pulsas Submit.
8. **Después** — recibo, portabilidad, inicio de nómina, public access file, cómo leer el correo de aprobación, comprobación del I-797A.

## Instalación

| Host | Cómo |
|---|---|
| Claude.ai / Claude de escritorio | Settings → Skills → sube el archivo `.skill`, o envíalo en un chat y pulsa *Save skill* |
| Claude Code | copia la carpeta a `~/.claude/skills/h1b-founder-self-petition/` |
| Codex CLI | copia la carpeta a `~/.codex/skills/h1b-founder-self-petition/` (mismo formato SKILL.md) |
| ChatGPT | crea un Custom GPT, pega `adapters/chatgpt-custom-gpt.md` en Instructions y sube `references/*` y `templates/*` como Knowledge |

Rellenar el formulario requiere la extensión **Claude in Chrome** con permiso para `my.uscis.gov`. Todo lo demás funciona sin navegador. `adapters/README.md` compara lo que puede hacer cada host.

## Estructura

```
SKILL.md                      el flujo que sigue la IA
references/                   clave de respuestas del I-129, mapa de pruebas, lista de coherencia, automatización de Chrome, tasas, preparación de la LCA, después de presentar, base legal, lecciones del caso real
templates/                    esquema y ejemplo de case.json, carta de apoyo, descripción del puesto, carta de oferta, contrato laboral, resolución del consejo, esquema de plan de negocio, textos del formulario
adapters/                     Instructions para un Custom GPT de ChatGPT, comparación de hosts
scripts/                      validate_case.py (validación), render_templates.py (plantillas)
```

## Probar los scripts

```bash
python scripts/validate_case.py templates/case.example.json
python scripts/render_templates.py templates/case.example.json --out drafts/ --docx
```

## Alcance

Cambio de empleador / extensión / transferencia exenta de cap para un fundador que ya está en EE. UU. en estatus H-1B y tiene una LCA certificada. El registro para la lotería, el trámite consular y L-1/O-1 quedan fuera. Las tasas y el diseño del formulario cambian; la skill indica a la IA que los verifique en uscis.gov.

Es una herramienta para preparar tu propia petición, no asesoramiento legal.

## Licencia

MIT
