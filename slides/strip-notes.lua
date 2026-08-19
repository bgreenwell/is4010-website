-- Speaker notes are instructor-only. Keep them in the revealjs decks and drop them from
-- every other format, notably the ipynb companion notebooks handed to students.
function Div(el)
  if el.classes:includes("notes") and FORMAT ~= "revealjs" then
    return {}
  end
end
