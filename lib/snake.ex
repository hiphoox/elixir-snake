defmodule Snake do
  use Application

  def start(_type, _args) do
    Snake.Supervisor.start_link
  end

end
